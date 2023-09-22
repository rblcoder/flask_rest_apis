FROM python:3.9-slim

COPY . /opt/
WORKDIR /opt

RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]

