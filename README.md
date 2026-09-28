# Django Online Course - Final Project

This is the Django-based Online Course application built as part of the IBM Coursera final project.

## Project Structure

```
onlinecourse/
├── models.py        # Question, Choice, Submission models
├── admin.py         # Admin configuration with inline models
├── views.py         # submit and show_exam_result views
├── urls.py          # URL patterns for exam submission
└── templates/
    └── onlinecourse/
        ├── course_list_bootstrap.html
        ├── course_details_bootstrap.html
        ├── exam_result_bootstrap.html
        ├── user_login_bootstrap.html
        └── user_registration_bootstrap.html
```

## Setup Instructions

1. Install dependencies:
```bash
pip install django pillow
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Seed the database:
```bash
python seed_data.py
```

4. Run the server:
```bash
python manage.py runserver
```

## Credentials

- **Admin**: username=`admin`, password=`admin123`
- **Test User**: username=`testuser`, password=`test123`

## URLs

- Homepage: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Assessment Feature

The app includes the following assessment models:
- **Question**: Each question belongs to a Lesson and has a grade value
- **Choice**: Each choice belongs to a Question and can be marked as correct
- **Submission**: Records a user's exam attempt with their selected choices

The `submit` view processes exam submissions, and `show_exam_result` calculates and displays the score with a "Congratulations!" message if the user scores 70% or above.
