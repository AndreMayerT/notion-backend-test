FROM python:3.10.9

WORKDIR /workspace

COPY . .

RUN pip install -r requirements.txt

RUN python3 manage.py runserver