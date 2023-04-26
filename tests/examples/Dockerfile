FROM python:3.10
WORKDIR /app
COPY ./tests/examples .
RUN pip install -r requirements.txt
#COPY ./findmyorder/core.toml .
EXPOSE 8443 8080
CMD [ "python", "./example.py" ]
