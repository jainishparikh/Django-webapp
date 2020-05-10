FROM python:3.6.10-buster
COPY . .
EXPOSE 3306
EXPOSE 8000
WORKDIR /whatsbusy
RUN pip install -r requirement.txt
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000


# sudo docker run -d -p 3306:3306 -e MYSQL_PASSWORD=jainish -e MYSQL_USER=jainish -e MYSQL_DATABASE=whatsbusy -e MYSQL_ROOT_PASSWORD=root --name=mysql mysql:5.7

# sudo docker run -it --link=mysql -p 8000:8000 -e PASSWORD=jainish -e USER=jainish -e DATABASE=whatsbusy -e HOST=mysql -e PORT=3306 --name=whatsbusy jainishparikh/whatsbusy:v1  