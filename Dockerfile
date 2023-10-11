FROM python:3.9-slim-buster
RUN apt update -y && apt upgrade -y 
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8080
CMD ["python", "app.py"]