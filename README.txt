- django project init/create
django-admin startproject core .

- build a store by starting the app; store is the name of the app
py manage.py startapp store

- add the app (here it is store) name in core/settings.py under the apps list which should be around the middleware list

- once the initial models are added, install dependencies
    Import User class from django.contrib.auth.models; install Pillow

- make the migrations
    ./manage.py makemigrations
    ./manage.py migrate

- to store the images in the images folder/, create a new folder named media in the project directory

- in the settings.py file, add two new variables called MEDIA_URL='/media/' and MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

- the following code snippet is added in urls.py
 if settings.DEBUG: # runs only if it is in development environment
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # adds a static file route that is pointing to the media root directory for accessing static resources/assets

- now in admin.py, some products, categories, etc will be added to populate the database

- run './manage.py createsuperuser' with username as github username, email address, password (on local system keep password blank)