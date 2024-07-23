FROM python:3.12

RUN pip install flask gunicorn

COPY . .

ENV PYTHONUNBUFFERED=true

CMD ["gunicorn", "-b", ":8080", "main:app"]


