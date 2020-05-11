
# Django-webapp:
This a initial Django web-application which enables users to manage subscriptions using Stripe and Django 2.2. 


### Steps To-do before starting application:
Update setting.py file in ./whatsbusy/whatsbusy/settings.py
- Insert database information for MYSQL (create a database and save database name, username and password for MYSQL)
- Create a free Stripe account and gather your API credentials.
- Insert your STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY.

### Steps to run the application on localhost:
```sh
cd whatsbusy
pip install -r requirement.txt
```
  (make sure to setup mysql and settings.py file mentioned above before moving forward)
```sh
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
(default port is 8000)

Go to http://localhost:8000/    

### Steps to run the application in Docker:
##### Make sure Docker is installed and running.

(add the values to the environments variables in the command below as you like)
```sh
docker run -d -p 3306:3306 -e MYSQL_PASSWORD= -e MYSQL_USER= -e MYSQL_DATABASE= -e MYSQL_ROOT_PASSWORD= --name=mysql mysql:5.7
```
(add the values to envirnment variables same as added in the above command)
```sh
docker run -d --link=mysql -p 8000:8000 -e PASSWORD= -e USER= -e DATABASE= -e HOST=mysql -e PORT=3306 --name=whatsbusy jainishparikh/whatsbusy   
```

##### Corresponding Environment Variables in both docker commands:
 `MYSQL_PASSWORD` = `PASSWORD`
`MYSQL_USER` = `USER`
`MYSQL_DATABASE` = `DATABASE`

Go to http://localhost:8000/  