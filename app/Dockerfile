FROM python:3.14-alpine3.22

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt


ENV PORT=5000 

CMD ["python", "app.py"]
