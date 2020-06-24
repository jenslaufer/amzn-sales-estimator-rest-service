FROM python:3.7

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY settings.py settings.py

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD [ "python", "app.py" ]