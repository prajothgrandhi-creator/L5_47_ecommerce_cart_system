# Lab 5: Static Code Analysis — Issue Log

Repository: `SETAPESU26/L5_47_ecommerce_cart_system`  
Program: `ecommerce_cart_system.py`

The line numbers below refer to the **original starter program** before fixes. Findings were collected from the original Pylint, Bandit, and Flake8 reports.

| Issue | Type / Tool | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Unsafe dynamic expression evaluation | Security — Bandit B307; Pylint W0123 | 44 | `eval(discount_expr)` could execute arbitrary Python code rather than just calculate a discount. | Removed `eval()`. The revised function accepts a numeric discount rate, validates it is between 0 and 1, and calculates the total directly. |
| Weak MD5 hash | Security — Bandit B324 | 49 | MD5 is not appropriate where a stronger hash is needed. | Replaced MD5 with SHA-256. |
| Shell command execution | Security — Bandit B605 | 60 | `os.system()` launched a shell to print the receipt message, creating unnecessary shell-injection risk. | Removed shell execution and used Python's `print()`. |
| Insecure pseudo-random PIN | Security — Bandit B311 | 53 | `random.randint()` is not intended for security-sensitive values. | Replaced it with `secrets.randbelow()` to generate a four-digit PIN. |
| Mutable default argument | Correctness / code quality — Pylint W0102 | 15 | `audit_log=[]` reuses the same list between calls when no list is passed. | Changed the default to `None` and initializes a new list inside the function. |
| Bare exception and swallowed errors | Reliability — Pylint W0702; Bandit B110; Flake8 E722 | 27–29 | A bare `except:` followed by `pass` hides every error, not just a missing item. | Catches `KeyError` only and returns `False` when the item does not exist. |
| File handling without context manager or encoding | Code quality — Pylint W1514, R1732 | 57–59 | The file was opened without an explicit encoding and manually closed. | Uses `Path.open()` with UTF-8 encoding and a `with` block. |
| Unused import | Code quality — Pylint W0611; Flake8 F401 | 4 | `math` was imported but not used. | Removed the unused import. |
| Unused variables | Code quality — Pylint W0612; Flake8 F841 | 33, 43, 65 | Variables such as `handling_fee`, `base_price` in the original expression-based implementation, and loop variable `k` were unused. | Removed unused variables and simplified the cart summary. |
| Comparison with `None` | Style — Pylint C0121; Flake8 E711 | 34 | The original code used `== None`. | Replaced the check with the idiomatic `is None` logic as part of simplifying the status check. |
| Naming, docstrings, and formatting | Maintainability/style — Pylint C0103, C0114, C0116, C0304; Flake8 E501, W292 | Multiple | Several function names were not snake_case, documentation was missing, a line was too long, and the file lacked a final newline. | Renamed functions to snake_case, added docstrings, formatted long lines, and ensured the file ends with a newline. |
| Hard-coded secret-like value printed to console | Security — manual code review | 72 | The original program contained a hard-coded payment-gateway secret-like string and printed it. This was visible in program output even though it was not necessarily flagged by these analyzer reports. | Removed the hard-coded value and its print statement. Real credentials should be stored outside source code, such as in environment variables or a secrets manager. |

## Verification results

- Original Pylint score: **3.86/10**
- Revised Pylint score: **10.00/10**
- Revised Bandit report: **No issues identified** (0 high, 0 medium, 0 low)
- Revised Flake8 report: **No output**, indicating no reported Flake8 violations

These results are based on the reports generated for the revised file during this lab. Static analysis is helpful, but it does not prove that every possible functional or security problem has been eliminated.
