# Dockerfile

# pull the official docker image
FROM python:3.11.1-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV JWT_SECRET=_JWT_SECRET

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
####for GCP
# EXPOSE 8080
# copy project
COPY . .
####for GCP
# CMD exec uvicorn app.main:app --host=0.0.0.0 --port=8080 --workers=1