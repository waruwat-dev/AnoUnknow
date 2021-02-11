(optional) goto mysite/setting 
-DATABASES
-CHANNEL_LAYERS


run command follow by this list

1.docker run -p 6379:6379 -d redis:5

2.pip install -r requirements.txt

3.python manage.py migrate

4.python manage.py createsuperuser 
(optional) for create admin user if u want to be admin for django for view in django db, etc(not associate with my project)
and goto localhost:8000/admin

5.python manage.py runserver