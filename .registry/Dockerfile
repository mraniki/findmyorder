FROM python:3.11
WORKDIR /app
#COPY ./examples/ /.requirements/requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

COPY ./examples/ .
RUN pip install --no-cache-dir findmyorder
RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir uvicorn

EXPOSE 8080
CMD [ "python", "./example.py" ]
