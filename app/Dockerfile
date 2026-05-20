FROM python:3.14-alpine3.22

# указание рабочего каталога внутри контейнера
WORKDIR /app

# копирование файлов
COPY . /app
# установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# запуск приложения
CMD ["python", "app.py"]
