FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/actions-runner/_work/trendyol-backend-v2/trendyol-backend-v2

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip3 install -r requirments.txt
RUN pip3 install django-createsuperuserwithpassword
