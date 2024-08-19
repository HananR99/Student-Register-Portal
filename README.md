## Student Register Portal
Student Register Portal is a Python Django project designed to implement CRUD (Create, Read, Update, Delete) operations. 
This project serves as a registration system for students, allowing administrators to manage student data efficiently.
## Features
- **Student Registration**: Can register new students with details such as name, id, mobile and department.
- **Student Management**: Allows updating and deleting student records.
- **Bootstrap 4 Integration**: Uses `django-bootstrap4` for a responsive and modern UI.
- **Crispy Forms**: Utilizes `django-crispy-forms` for enhanced form rendering.

![image](https://github.com/user-attachments/assets/508ebfd7-f7e9-40dd-b6d1-8d46ca4f866e)
set up with superuser for admin purposes
![image](https://github.com/user-attachments/assets/0e5d84a2-cec2-4613-95be-d4402616ebde)
![image](https://github.com/user-attachments/assets/6b6a9e5e-5d84-4548-994f-9bb3c2e06e47)
If not authenticate can't get to those pages.

### Prerequisites

- Python 3.9+
- Django 4.2+
- `django-crispy-forms` and `django-bootstrap4`

## Installation

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd student_portal

2. pip install django psycopg2-binary crispy-forms
3. Ensure that PostgreSQL is installed and running on your system. Update your database settings in student_portal/settings.py
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver

Open your web browser and go to http://127.0.0.1:8000/ to view the application.
