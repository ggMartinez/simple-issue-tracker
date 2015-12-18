# Simple Issue Tracking

Simple Issue Tracking is a software for tracking issue tickets, made enterily with Django Admin App.

It requires Django 1.9 and Python 3. For database, you can use the database engines supported by Django.

# Database Configuration
Rename(or copy) the file "Database_settings.py.sample" into "Database_settings", and configure it to use the database you want. (see https://docs.djangoproject.com/en/1.9/ref/settings/#databases )

After that, excecute "python3 manage.py migrate" to create the database, and "python3 manage.py createsuperuser" to create the Super User for the system.

# Users and groups.

There's no usergroups by default. You have to manually add the permissions for the "Ticket" model for the users in the Django admin, or define a group, give it the permissions, and then assign the group for the Users.


