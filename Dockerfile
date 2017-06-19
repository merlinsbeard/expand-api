FROM python:3.6.1
WORKDIR .
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000:5000
CMD gunicorn app:app.wsgi --workers=4 --bind=0.0.0.0:5000
