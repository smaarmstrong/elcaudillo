FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./ 
