FROM python:3.12-slim

# Set environment Variable

ENV PYTHONDONTWRITEBYTECODE=1
ENV PUTHONUNBFFERED=1

#set work directory

WORKDIR /app

#Install system dependencies

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

#Install python dependencies

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

#Copy Project

COPY . .

#Collect static file

RUN python manage.py collectstatic --noinput || true

#Run gunicorn

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "ams_project.wsgi:application"]
