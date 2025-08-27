# 🔐 Password Strength Checker  

A simple Python tool that checks the **strength of your password** based on commonly accepted security standards.  

It validates whether the password contains:  
- ✅ At least **8 characters**  
- ✅ At least **1 digit**  
- ✅ At least **1 uppercase letter**  
- ✅ At least **1 lowercase letter**  
- ✅ At least **1 special character**  

---

## 📂 Features
- Real-time password strength checking  
- Categorizes passwords as **Weak, Medium, or Strong**  
- Provides a **strength score (0–5 stars)**  
- Supports exit option (`exit`) to quit the tool  
- Lightweight & beginner-friendly  

---

## 🛠️ Requirements
- Python 3.x  
- No external dependencies (uses only `re` module from standard library)  

---

## 🚀 Usage

### 1. Clone this repository
```bash
git clone https://github.com/your-username/password-checker.git
cd password-checker

### 2. Run the script
```bash
python password_checker.py

-> Welcome to the Password Strength Checker Tool
Enter your password (or type 'exit' to quit): hello
Weak (★☆☆☆☆): password must be at least 8 characters long

Enter your password (or type 'exit' to quit): Hello123
Medium (★★★☆☆): password must contain a special character

Enter your password (or type 'exit' to quit): Hello@123
Strong (★★★★★): password is secured!

