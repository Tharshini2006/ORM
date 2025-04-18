# Ex02 Django ORM Web Application
## Date: 12.04.2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).
## ENTRY RELATIONSHIP DIAGRAM
![image](https://github.com/user-attachments/assets/3ab47a6c-a901-4e9f-844d-2c7fb7cc154f)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```python
    admin.py

    from django.contrib import admin
    from .models import Movie,MovieAdmin

    admin.site.register(Movie,MovieAdmin)
    
    models.py

    from django.db import models
    from django.contrib import admin

    class Movie(models.Model):
    user_id = models.CharField(max_length=20, help_text="User ID")
    user_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=15)
    movie_name = models.CharField(max_length=200)
    show_datetime = models.DateTimeField()
    no_of_seats = models.IntegerField()

    class MovieAdmin(admin.ModelAdmin):
      list_display = ('user_id', 'user_name', 'email_id', 'phone_number', 'movie_name', 'show_datetime', 'no_of_seats')
```
## OUTPUT
![alt text](<WhatsApp Image 2025-04-12 at 12.52.57_32a65032.jpg>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
