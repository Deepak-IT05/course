
## FUNCTIONS
## Student
- Student can view/search Courses without login.
- When Student try to joining these courses, then he/she must login to system.
- Then Registered details and Selected the courses
- Student can send feedback to admin (without login)
---
### Admin
- First admin will login ( for username/password run following command in cmd )
```
py manage.py createsuperuser
```
- Give username, email, password and your admin account will be created.
- After login, there is a dashboard  where admin can see how many Student is registered, how many Courses are there.
- Admin can add/delete/view/edit the Courses.
- Admin can view/edit/delete Student details.
- Admin can view/delete/edit course details.
- Admin can view the feedbacks sent by customers.
---
## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
pip install django==3.0.5
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'

ALTERNATE LOGIN
USERNAME="admin"
PASSWORD="deepak"
```

## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Contributor
-https://github.com/Deepak-IT05

## Feedback
Any suggestion and feedback is welcome. You can message me on Instagram
