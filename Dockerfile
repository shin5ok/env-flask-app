FROM python:3.12

RUN pip install flask gunicorn

COPY . .

CMD ["gunicorn", "-b", ":8080", "main:app"]


