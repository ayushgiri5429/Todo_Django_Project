from django.db import models

# If there is any change in models.py, run following:
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Todo(models.Model): #pascalCase
    title = models.CharField(max_length=200) # varchar, char

    def __str__(self):
        return self.title