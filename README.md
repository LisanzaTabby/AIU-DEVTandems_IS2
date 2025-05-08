
# AIU Developers-Connection Platform (AIUDEVTANDEMS)

![Uploading image.png…]()


## 📘 Project Overview

The AIU Developers-Connection Platform (AIUDEVTANDEMS) is a web-based peer-learning system developed to support Information Technology students at Africa International University (AIU). It enables students to connect with peers proficient in various programming languages, collaborate on course projects, and access structured support — thereby reducing delays in project completion and improving academic outcomes.

The platform is grounded in AIU’s Christ-centered mission and promotes servant leadership by encouraging mentorship and collaborative learning among students.

## 🚀 Features

- 🔐 Secure user registration and login with social authentication (Google & GitHub)
- 👤 Profile management: programming languages known, bio, and interests
- 📚 Categorized study rooms by programming language (e.g., Python, JavaScript, Web3)
- 💬 Real-time chat and messaging within rooms
- 🔍 Search and filter rooms by topic or language
- 📧 Email notifications for new messages
- ⚙️ Admin dashboard via Django Admin
- 📈 Scalable architecture for future feature expansion

## 🛠️ Built With

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Django Templates
- **Database:** PostgreSQL
- **Authentication:** Django-Allauth (Google & GitHub OAuth)
- **Version Control:** Git & GitHub
- **Database Management:** pgAdmin4
- **Design Tools:** Draw.io (UML, ERD)

## 📦 Installation Guide

### Prerequisites

- Python 3.9+
- PostgreSQL 15+ or SQLite (for local testing)
- Git
- Virtual Environment (`venv`)
- Visual Studio Code (or preferred IDE)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/LisanzaTabby/AIU-DEVTandems_IS2.git
   cd AIU-DEVTandems_IS2
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv Env
   Env\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file and include:
   ```env
   OAUTH_GOOGLE_CLIENT_ID=your-google-client-id
   OAUTH_GOOGLE_CLIENT_SECRET=your-google-secret
   OAUTH_GITHUB_CLIENT_ID=your-github-client-id
   OAUTH_GITHUB_SECRET=your-github-secret
   DATABASE_NAME=devtandems_db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=yourpassword
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

5. **Run Migrations and Create Superuser**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Platform**
   Open your browser and go to: `http://127.0.0.1:8000/`

## 🧪 Testing

The platform was tested through both **unit tests** and **validation testing** to verify:
- Input validation
- CRUD operations
- Social login functionality
- Notifications and messaging

Test plans are documented in the `/docs` or Appendix section of the project report.

## 📝 License

This project is developed for academic purposes and is not licensed for commercial use.

## 🤝 Acknowledgements

- Africa International University (AIU)
- Lecturer Jared Maranga Mayieka
- Django, PostgreSQL, and Django-Allauth open-source communities
