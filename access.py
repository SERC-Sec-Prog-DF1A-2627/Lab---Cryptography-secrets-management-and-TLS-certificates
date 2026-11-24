"""Provided classroom sign-in. Only the server assigns the staff identity."""
import hmac
import secrets

from flask import abort, redirect, render_template, request, session, url_for


def new_codes() -> dict[str, str]:
    return {staff: secrets.token_urlsafe(8) for staff in ("alex", "sam")}


def register_access(app, codes: dict[str, str]) -> None:
    @app.before_request
    def check_form():
        # Every form carries an unpredictable session-bound CSRF token.
        if "csrf" not in session:
            session["csrf"] = secrets.token_hex(24)
        if request.method == "POST":
            supplied = request.form.get("csrf", "").encode()
            if not hmac.compare_digest(session["csrf"].encode(), supplied):
                abort(400)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        error = None
        if request.method == "POST":
            staff = request.form.get("staff", "")
            code = request.form.get("code", "").encode()
            if staff in codes and hmac.compare_digest(codes[staff].encode(), code):
                session.clear()
                session["staff"] = staff
                session["csrf"] = secrets.token_hex(24)
                return redirect(url_for("notes"))
            error = "Check the staff name and the code from this server run."
        return render_template("login.html", error=error, staff_names=codes.keys())

    @app.post("/logout")
    def logout():
        session.clear()
        return redirect(url_for("login"))
