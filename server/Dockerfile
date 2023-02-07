FROM python:latest

RUN apt-get update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
CMD ["python3", "./EASY-EATS-APP.py"]