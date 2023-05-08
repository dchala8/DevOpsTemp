# Empezar corriendo una imagen de python 
FROM python:3.10.6
env FLASK_APP=application.py

WORKDIR /app
COPY . /app/
    
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "application.py"]