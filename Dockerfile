FROM python:3.11.2-alpine3.16

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

WORKDIR /usr/app

CMD [ "python", "-m", "bot" ]