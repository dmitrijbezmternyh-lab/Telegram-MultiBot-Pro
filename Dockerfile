FROM python:3.11-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копирование зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание непривилегированного пользователя
RUN useradd -m botuser && chown -R botuser:botuser /app
USER botuser

CMD ["python", "-m", "bot.main"]
