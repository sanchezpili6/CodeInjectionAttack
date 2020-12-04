FROM python:2

WORKDIR /usr/src/app

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/app
RUN apt-get update
RUN apt install python-pip -y
RUN apt-get -y install apt-utils


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV DISPLAY=0
CMD [ "python", "main.py" ]