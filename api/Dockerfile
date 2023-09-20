FROM python:3.11-slim

WORKDIR /app

COPY api/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY api/inschooltech_test/ .

CMD ["gunicorn", "inschooltech_test.wsgi:application", "--bind", "0:8000" ]