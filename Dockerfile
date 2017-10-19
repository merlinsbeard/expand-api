FROM python:3.6.1
COPY . .
COPY requirements.txt ./
WORKDIR .
RUN pip install -r requirements.txt
EXPOSE 5000
RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["sh", "./entrypoint.sh"]
