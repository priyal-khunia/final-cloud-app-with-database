"""
Script to seed the database with test data for the OnlineCourse app.
Run with: python seed_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import (
    Course, Lesson, Instructor,
    Question, Choice, Enrollment
)

print("Seeding database...")

# Create superuser (admin)
if not User.objects.filter(username='admin').exists():
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123',
        first_name='Admin',
        last_name='User'
    )
    print("[OK] Created admin user (username: admin, password: admin123)")
else:
    admin_user = User.objects.get(username='admin')
    print("[--] Admin user already exists")

# Create a test learner user
if not User.objects.filter(username='testuser').exists():
    test_user = User.objects.create_user(
        username='testuser',
        password='test123',
        first_name='Test',
        last_name='Learner'
    )
    print("[OK] Created test user (username: testuser, password: test123)")
else:
    test_user = User.objects.get(username='testuser')
    print("[--] Test user already exists")

# Create instructor
if not Instructor.objects.filter(user=admin_user).exists():
    instructor = Instructor.objects.create(
        user=admin_user,
        full_time=True,
        total_learners=100
    )
    print("[OK] Created instructor")
else:
    instructor = Instructor.objects.get(user=admin_user)
    print("[--] Instructor already exists")

# Create a course
if not Course.objects.filter(name='Introduction to Python').exists():
    course = Course.objects.create(
        name='Introduction to Python',
        description='Learn Python programming from scratch. Master variables, loops, functions, and more!',
        pub_date='2024-01-01',
        total_enrollment=0,
    )
    course.instructors.add(instructor)
    print("[OK] Created course: Introduction to Python")
else:
    course = Course.objects.get(name='Introduction to Python')
    print("[--] Course already exists")

# Create lessons
lesson_data = [
    {
        'title': 'Python Basics',
        'order': 1,
        'content': 'Python is a high-level, interpreted programming language known for its simplicity and readability. In this lesson we cover variables, data types, and basic operations.',
    },
    {
        'title': 'Control Flow and Loops',
        'order': 2,
        'content': 'Learn how to control the flow of your programs using if/else statements, for loops, and while loops.',
    },
]

lessons = []
for ld in lesson_data:
    lesson, created = Lesson.objects.get_or_create(
        title=ld['title'],
        course=course,
        defaults={'order': ld['order'], 'content': ld['content']}
    )
    lessons.append(lesson)
    if created:
        print(f"[OK] Created lesson: {lesson.title}")
    else:
        print(f"[--] Lesson already exists: {lesson.title}")

# Create questions and choices for Lesson 1
if not Question.objects.filter(lesson=lessons[0]).exists():
    q1 = Question.objects.create(
        lesson=lessons[0],
        content='What is the correct way to define a variable in Python?',
        grade=50
    )
    Choice.objects.create(question=q1, content='var x = 5', is_correct=False)
    Choice.objects.create(question=q1, content='x = 5', is_correct=True)
    Choice.objects.create(question=q1, content='int x = 5;', is_correct=False)
    Choice.objects.create(question=q1, content='define x = 5', is_correct=False)
    print("[OK] Created question 1 with choices")

if not Question.objects.filter(lesson=lessons[1]).exists():
    q2 = Question.objects.create(
        lesson=lessons[1],
        content='Which keyword is used to create a loop that iterates over a sequence in Python?',
        grade=50
    )
    Choice.objects.create(question=q2, content='while', is_correct=False)
    Choice.objects.create(question=q2, content='loop', is_correct=False)
    Choice.objects.create(question=q2, content='for', is_correct=True)
    Choice.objects.create(question=q2, content='iterate', is_correct=False)
    print("[OK] Created question 2 with choices")

# Enroll the test user in the course
if not Enrollment.objects.filter(user=test_user, course=course).exists():
    Enrollment.objects.create(user=test_user, course=course, mode='honor')
    course.total_enrollment += 1
    course.save()
    print("[OK] Enrolled testuser in the course")

print("")
print("="*50)
print("[DONE] Database seeding complete!")
print("="*50)
print("")
print("Admin credentials: username=admin, password=admin123")
print("Test user credentials: username=testuser, password=test123")
print("")
print("Admin site: http://127.0.0.1:8000/admin/")
print("Course site: http://127.0.0.1:8000/")
