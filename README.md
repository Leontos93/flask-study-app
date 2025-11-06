# 📘 Flusk Study App

A simple **Flask CRUD (Create, Read, Update, Delete)** application built for learning purposes.  
This project demonstrates how to structure a Flask app, work with SQLAlchemy, and use Flask-WTF forms.

---

## 🚀 Features
- Create, edit, view, and delete books 📚  
- Flask-WTF form validation  
- SQLite database (configurable)  
- Flash messages and clean HTML templates  
- Ready to deploy to **Heroku** or any Flask-compatible platform

---

## 🧱 Project Structure
```

flusk-study-app/
├── app.py
├── models.py
├── forms.py
├── config.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
├── base.html
├── index.html
├── create.html
├── update.html
└── detail.html

````

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Leontos93/flusk-study-app.git
cd flusk-study-app
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///app.db
```

### 5. Run the application

```bash
flask run
```

App will be available at 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🛠 Technologies Used

* **Flask 3.x**
* **Flask-WTF**
* **Flask-SQLAlchemy**
* **WTForms**
* **Gunicorn (for deployment)**

---

