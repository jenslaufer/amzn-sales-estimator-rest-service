FROM python:3.7

COPY requirements.txt requirements.txt
COPY fiverr fiverr
COPY app.py app.py
COPY settings.py settings.py
COPY uwsgi.ini app.ini

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "uwsgi", "--ini", "app.ini" ]