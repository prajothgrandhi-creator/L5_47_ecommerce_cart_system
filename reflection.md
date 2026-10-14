# Lab 5: Static Code Analysis — Reflection

**Important:** The uploaded four-page handout refers to reflection questions but does not show the actual four questions. These are draft reflection answers organized around the lab's stated learning outcomes. If your instructor provided the exact questions separately, match these answers to those questions before submitting.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and style problems. It is useful because it helps detect problems early, improves maintainability, and gives developers consistent feedback before code is delivered.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality, naming, documentation, and possible programming mistakes. Bandit focuses on common Python security risks, such as unsafe expression evaluation, weak hashing, and shell execution. Flake8 checks style and common code issues, including unused imports, bare exceptions, and formatting violations. Using all three gives complementary views of the same program.

## 3. What important issues did you identify and fix?

The original program used `eval()` to calculate a discounted price, used MD5 for item hashing, invoked a shell command to print a receipt message, used `random` for a checkout PIN, used a mutable default list, and silently ignored all exceptions when removing items. I replaced `eval()` with validated numeric discount calculation, used SHA-256 and `secrets`, removed shell execution, corrected the default argument, and handled `KeyError` explicitly. I also improved file handling, naming, documentation, and formatting.

## 4. How did static analysis improve the code, and what are its limitations?

The original Pylint score was 3.86/10. After the fixes, it reached 10.00/10. The revised Bandit report identified no issues, and Flake8 produced no output. These checks made the code cleaner and addressed the reported security and style findings. However, static-analysis tools cannot prove that a program is completely correct or secure, so the program should still be tested with normal, boundary, and invalid inputs, and the findings should be reviewed rather than blindly followed.
