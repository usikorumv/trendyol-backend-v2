FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/actions-runner/_work/trendyol-backend-v2/trendyol-backend-v2

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r requirments.txt
