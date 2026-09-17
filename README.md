\# Password Security Checker



A beginner-friendly Python command-line tool that checks password strength based on length and character composition.



\## About



Password Security Checker analyzes a password locally and gives it a simple strength score.



The program checks whether a password contains:



\* Lowercase letters

\* Uppercase letters

\* Numbers

\* Special characters

\* A sufficient length



It then calculates a score from \*\*0 to 7\*\* and classifies the password as:



\* Weak

\* Moderate

\* Strong



This project was built to practice Python fundamentals and explore basic defensive cybersecurity concepts.



\## ✨ Features



\* Password strength scoring

\* Hidden password input using Python's `getpass`

\* Lowercase character detection

\* Uppercase character detection

\* Number detection

\* Special character detection

\* Password length checking

\* Suggestions for missing requirements

\* Simple command-line interface

\* Passwords are not stored by the program



\## 🛠️ Technologies



\* Python 3

\* Python Standard Library

\* `string`

\* `getpass`



\## 📂 Project Structure



```text

password-security-checker/

│

├── password\_checker.py

└── README.md

```



\## 🚀 How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR-USERNAME/password-security-checker.git

```



\### 2. Enter the project directory



```bash

cd password-security-checker

```



\### 3. Run the program



```bash

python password\_checker.py

```



\## 💻 Example



The password is hidden while typing.



```text

Enter your password:



Password is strong!

Password score:7/7

```



For a weaker password:



```text

Enter your password:



Password is weak!

Password score:2/7



Missing an uppercase letter!

Missing a special character!

Missing a digit!

```



Type:



```text

exit

```



to close the program.



\##  Scoring System



| Requirement       | Points |

| ----------------- | -----: |

| 12+ characters    |     +3 |

| 8–11 characters   |     +2 |

| Lowercase letter  |     +1 |

| Uppercase letter  |     +1 |

| Digit             |     +1 |

| Special character |     +1 |



\### Strength Levels



| Score | Strength |

| ----: | -------- |

|   0–2 | Weak     |

|   3–4 | Moderate |

|   5–7 | Strong   |



\##  Security Notes



This project is intended for educational purposes.



Passwords are processed locally and are not stored or transmitted by the program.



The scoring system is a simple heuristic and should \*\*not\*\* be considered a complete measure of real-world password security.



For example, a password can satisfy the character requirements while still being predictable or commonly used.





\##  Future Improvements



Possible future versions could include:



\* Password generator

\* Better password-strength analysis

\* Common-password detection

\* Password entropy estimation

\* Graphical user interface

\* Exportable security reports

\* Offline breached-password dataset checking



\## License



MIT License



