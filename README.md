# 🔐 Password Strength Checker

A simple Python-based **Password Strength Checker** with both **CLI** and **GUI** interfaces, ensuring users create secure passwords.

## 📌 Features

✅ **Password Strength Analysis:** Evaluates password security based on:
- Length (minimum 8 characters)
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Special characters (`!@#$%^&*()-_+=`)

✅ **Strength Levels:**
- **Very Strong** (5/5)
- **Strong** (4/5)
- **Moderate** (3/5)
- **Weak** (2/5)
- **Very Weak** (1/5)

✅ **User Feedback:** Provides suggestions on how to improve weak passwords.

✅ **Graphical User Interface (GUI):** Simple Tkinter-based interface for ease of use.

✅ **Command-Line Interface (CLI):** Runs in the terminal for quick password strength checks.

## 🛠️ Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Pmvita/Password-Strength-Checker.git
   cd Password-Strength-Checker
   ```

2. **Ensure Python is installed** (Python 3.7+ required).  
   Check your version:
   ```sh
   python --version
   ```

3. **Install required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(Note: If `requirements.txt` is missing, dependencies can be installed manually: `pip install tk`.)*

## 🚀 Usage

### CLI Mode:

Run the script in the terminal:
```sh
python main.py
```
Enter a password when prompted, and it will display the strength level and suggestions.

### GUI Mode:

Run the GUI version:
```sh
python gui.py
```
- Enter a password in the input field.
- Click the "Check Strength" button.
- A popup will show the password's security level and feedback.

## 🖥️ Example Outputs

**CLI Output Example:**
```
Enter a password: pass123
Password Strength: Weak (2/5)
Feedback:
- Password should be at least 8 characters long.
- Password should contain at least one uppercase letter (A-Z).
- Password should contain at least one special character (!@#$%^&*()-_+=).
```

**GUI Output Example:**
- A pop-up window displays:
  ```
  Password Strength: Very Strong (5/5)
  ```

## 📂 File Structure

```
Password-Strength-Checker/
├── main.py         # CLI-based password strength checker
├── gui.py          # GUI-based password strength checker
├── README.md       # Documentation
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

## ✨ Author

Developed by **Pierre Mvita**  
GitHub: [@Pmvita](https://github.com/Pmvita)
