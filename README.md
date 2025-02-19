# django-cv-website

This is a Django-based CV website built using Django templates. It dynamically displays a resume in a structured format.


### Clone the Repository
First, clone the GitHub repository:

```bash
git clone https://github.com/clely19/django-cv-website.git
cd django-cv-website
```

---

### Install Dependencies
Ensure you have Python installed. Then, install Django:

```bash
pip install django
```

---
### Create a Django Project
Run the following command to create a new Django project:

```bash
django-admin startproject mycv
cd mycv
```

---
###  Create a Django App
Inside your project folder, create an app where you'll manage your CV:

```bash
python manage.py startapp cvapp
```

Register this app in mycv/settings.py by adding 'cvapp' to the INSTALLED_APPS list.
---
###  Create a Django Template for Your CV
Inside your app (cvapp), create a templates folder and a subfolder named cvapp and then, create an HTML file for your CV inside it and edit cv.html to add your CV content using Django template
```bash
mkdir -p cvapp/templates/cvapp
touch cvapp/templates/cvapp/cv.html
```

Register this app in mycv/settings.py by adding 'cvapp' to the INSTALLED_APPS list.
---
###  Create a Django View
In cvapp/views.py, define a function that will send CV data to the template:

---
###  Configure URLs and Run the Server and View Your CV
Modify mycv/urls.py to include your app's URLs and apply migrations and start the Django server.
```bash
python manage.py migrate
python manage.py runserver
```

---

### 5️⃣ View the CV
Open a web browser and visit:

```bash
http://127.0.0.1:8000/cv/
```

This will display the formatted CV.
