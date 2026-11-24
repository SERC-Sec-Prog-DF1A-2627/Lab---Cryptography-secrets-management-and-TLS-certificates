# Activity 1 · Which technique fits?

**15 minutes · Two pairs and one group of three, or work independently.** Help the college decide which protection belongs in five different places. For each case, identify the asset, pick a technique and say whose key or which trusted value makes it work. Name one thing the college would still need to protect.

**First 2 minutes.** Read the cases. In a trio, one person proposes, one records and one asks “What would make that assurance fail?” The challenger explains the decision back to the group. In a pair the recorder also challenges. Rotate after cases 2 and 4.

**Next 9 minutes.** Complete the table, one row at a time. Working alone, write a choice, challenge your own assumption and refine the reason. The [short introduction](../exercises/00-introduction.md) defines the techniques.

**Final 4 minutes.** Pick the row where you had most doubt. Explain why one plausible alternative leaves a requirement unmet. In a group, take turns explaining. Working alone, write or speak a two-sentence defence, then compare with the [exemplar](../solutions/activity-1/README.md).

**Worked example.** A technician compares a downloaded installer with a SHA-256 digest obtained through an independently authenticated release channel. A matching digest supports file integrity because the expected value is trustworthy. If both values came from an untrusted mirror, the comparison would say little about the publisher.

| Case | Decision, asset and reason | Key or trust assumption | Remaining risk |
|---|---|---|---|
| 1. The college must check a returning user’s password. Staff have no reason to recover the original. | | | |
| 2. An adviser needs to read a confidential note next week. Someone might copy the database backup. | | | |
| 3. Graduates receive a public college policy PDF. Any recipient should be able to check who signed it and whether its contents changed. | | | |
| 4. A staff browser sends a new confidential note to the college website over public Wi-Fi. | | | |
| 5. Two internal services share an integrity key. A third party can change a transfer file and the text beside it. Only the two services should be able to create a valid verification tag. The file may be readable. | | | |

**My defence of one choice**  
Case:  
My first choice and its trust assumption:  
Alternative considered and the requirement it leaves unmet:
