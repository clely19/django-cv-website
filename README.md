# django-cv-website

This is a Django-based CV website built using Django templates.


### Clone the Repository
Cloned the GitHub repository:

```bash
git clone git@github.com:clely19/django-cv-website.git
cd django-cv-website
```

---

### Install Dependencies
After Python installed. Then, install Django:

```bash
pip install django
```

---
### Create a Django Project
Created a new Django project:

```bash
python3 -m django startproject mycv
cd mycv
```

---
###  Create a Django App
Inside my project folder, created an app where I managed my CV and registered this app in mycv/settings.py by adding 'cvapp' to the INSTALLED_APPS list.

```bash
python3 manage.py startapp cvapp
```


---
###  Create a Django Template for My CV
Inside the app (cvapp), created a templates folder and a subfolder named cvapp and then, created an HTML file for my CV inside it and edit cv.html to add my CV content using Django template:
```bash
mkdir -p cvapp/templates/cvapp
touch cvapp/templates/cvapp/cv.html
```

---
###  Create a Django View
In cvapp/views.py, defined a function that will send CV data to the template:

---
###  Configure URLs and Run the Server and View My CV
Modified mycv/urls.py to include my app's URLs and applied migrations and started the Django server.
```bash
python3 manage.py migrate
python3 manage.py runserver
```

---

### View the CV
Opened a web browser and visited:

```bash
http://127.0.0.1:8000/cv/
```

This displayed my formatted CV.
