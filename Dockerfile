FROM python:2-alpine

RUN pip install gunicorn flask

ADD hello_skylocker.py hello_skylocker.py
ADD hello_skylocker/wsgi.py hello_skylocker/wsgi.py
ADD hello_skylocker/config.py /etc/gunicorn/config.py

ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["gunicorn", "--config=/etc/gunicorn/config.py"]
CMD ["hello_skylocker"]
