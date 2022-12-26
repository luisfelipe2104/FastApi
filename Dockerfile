FROM python:3.9-slim-buster

COPY ./config ./config 
COPY ./model ./model
COPY ./routes ./routes
COPY ./schemas ./schemas

COPY ./database.sqlite3 ./database.sqlite3
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

# sudo docker build -t fastapi .
# sudo docker run -p 3000:5000 fastapi
# http://localhost:3000/docs