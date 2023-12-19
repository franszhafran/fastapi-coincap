FROM python:3.11-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0" , "--port" , "80"]