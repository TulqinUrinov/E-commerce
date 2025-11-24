FROM python:3.13-slim

# Muhit o‘zgaruvchilar
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# Kutubxonalarni o‘rnatamiz
COPY r.txt .
RUN pip install --no-cache-dir -r r.txt

# Loyiha fayllarini image ichiga nusxalaymiz
COPY . /usr/src/app

