#!/bin/sh
set -e

# Function to create a superuser
create_superuser() {
    echo "Creating superuser"
    python manage.py shell <<EOF
from authentication.models import CustomUser
from django.db.utils import IntegrityError
try:
    CustomUser.objects.create_superuser(username='mahdi', email='mahdi.mahdi@gmail.com', password='erfan852')
    print("User created successfully!")
except IntegrityError:
    print("This user is already exist!")
EOF
}

sleep 5

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Run Tests
#python manage.py test

# Call the function
create_superuser;


# Run the application.
uwsgi --http=0.0.0.0:8001 --processes=5 --master --env=DJANGO_SETTING_MODULE=blog.settings --module=blog.wsgi:application
