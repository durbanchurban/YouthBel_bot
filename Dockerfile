FROM python:3.10-alpine

RUN mkdir /usr/app
WORKDIR /usr/app
COPY . /usr/app

RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]
