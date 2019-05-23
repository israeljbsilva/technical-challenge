FROM python:3.6-alpine3.6

COPY app.py /app/app.py
COPY routes /app/routes
COPY static /app/static
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD ["python", "app.py", "--debug"]