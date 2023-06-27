# django-blog

A Simple Blog Project Using Django Framework  Features used in this project :

* Set A Profile
* Manage Your Posts
* Like Posts
* Used Redis asn Cache backend 
* Used Session Framework 
* Used Message Framework 
* Send a Welcome Email using celery with Redis

How to run the project?

1:
  * install requirements.txt with command : pip install -r requirements.txt
  
2:
  * install Redis and make sure it's active and running
  
3:
  * Create a file with the name local_setting.py beside setting.py and add the following code:
  
  * SECRET_KEY = 'YOUR SECRET KEY'
  * DEBUG = True          # if you want to use this project in production change the value to False.
  * EMAIL = "YOUR EMAIL ADDRESS"
  * APP_PASSWORD = "YOUR APP PASSWORD"
  * ALLOWED_HOSTS = ['*']         # if you want to use this project in production replace your domain in that list.
  
4: 
  * Run python manage.py migrate
  * Run python manage.py createsuperuser

5:
  * run python manage.py runserver

6:
  * celery -A E_commerce worker -Q Bemail -l INFO   # if you don't run this, emails will not send to the users.

  
ENJOY THE PROJECT :)
    
