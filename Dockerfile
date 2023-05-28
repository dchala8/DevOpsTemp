# Empezar corriendo una imagen de python 
FROM python:3.10.6
ENV FLASK_APP=application.py

WORKDIR /app
COPY . /app/
    
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "application.py"]
RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="blacklist-C2J-cloud"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LICENSE_KEY=
ENV NEW_RELIC_LOG_LEVEL=info

ENTRYPOINT [ "newrelic-admin", "run-program" ]