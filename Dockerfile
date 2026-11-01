FROM docker.arvancloud.ir/python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -i https://mirror-pypi.runflare.com/simple -r requirements.txt
COPY . /app/

WORKDIR /app/core

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]