# How to Run the Flask App

Follow these steps to set up and run the Flask application:

---

## Prerequisites

Ensure you have the following installed:
- **Python** (version 3.7 or higher)
- **pip** (Python package manager)
- **Flask** (installed via pip)

---

## Instructions

### 1. Clone the Repository
If you haven't already, clone the project repository to your local machine.
```bash
git clone https://github.com/aidantiu/dsa_portfolio
```

### 2. Navigate to the Project Directory
Open your terminal and navigate to the `portfolio` directory:
```bash
cd portfolio
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Flask DotEnv
```bash
cd portfolio
touch .flaskenv
```
- Add Environment Variables to .flaskenv Open the file in your favorite text editor (e.g., nano, vim, or code) and add the following content:
```
FLASK_APP=run.py
```
### 5. Run Flask
```bash
cd portfolio
flask run
```