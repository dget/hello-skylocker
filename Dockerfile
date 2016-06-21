FROM python:2-alpine
ADD hello-skylocker.py hello-skylocker.py
CMD [ "python", "./hello-skylocker.py" ]
