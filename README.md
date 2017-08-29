# django_blog
A web blog in django framework

## Usage
* Check the following in settings.py  
  1. secret key
  2. DEBUG
  3. ALLOWED_HOSTS
* Make migration
  * python manage.py makemigrations
  * python manage.py migrate
* Create a super user
  * python manage.py createsuperuser
* Run the web app and create your new post in admin
  * python manage.py runserver
  * Go to http://\<your-domain\>/admin or http://127.0.0.1:8000/admin to create a new post
