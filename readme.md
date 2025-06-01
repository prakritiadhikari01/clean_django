# 🧩 Reusable Django Project – Day 8 Assignment

This is a beginner-friendly Django project demonstrating **code reusability** and **best practices**, as part of **Day 8** of the Beginner’s Web Dev Series.

## ✅ Key Features

- ✅ Reusable model mixin (`BaseTimestampModel`)
- ✅ Models: Post, Comment, Author, Category, Tag
- ✅ Environment variable setup using `python-decouple`
- ✅ GitHub version control with `.gitignore` and `.env.example`

---
## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/prakritiadhikari01/clean_django.git
   cd clean-django-project

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Create a .env file**
   ```bash
    DEBUG=True
    SECRET_KEY=your-secret-key


5. **Run migrations**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Run the development server**
   ```bash
    python manage.py runserver

# 📚 Models

All models inherit from `BaseTimestampModel` to keep timestamps consistent:

- **Post:** Stores blog post content.
- **Comment:** Linked to posts, includes name and content.
- **Author:** Optional author details.
- **Category:** Categorizes posts.
- **Tag:** Adds tag support for posts.

---

# 🛡️ Best Practices Followed

- DRY principle applied using abstract base classes  
- Sensitive info moved to `.env` file  
- Version-controlled with `.gitignore`  
- `.env.example` provided for teammates  

---

# 🔗 GitHub

📍 [GitHub Repository Link](#) *(https://github.com/prakritiadhikari01/clean_django)*

---

# 📅 Workshop Series

This project is part of the **Beginner’s Web Dev Django Workshop – Day 8: Reusability & Best Practices** hosted by Shankar Lamichhane.

---

# 👩‍💻 Author

Created with ❤️ by **Prakriti Adhikari**

---

