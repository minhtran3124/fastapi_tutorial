FROM python:3.9

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV APP_DIR /app

WORKDIR $APP_DIR

COPY requirements $APP_DIR/requirements

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . $APP_DIR

ENV PYTHONPATH=$APP_DIR

EXPOSE 8000

CMD ["python", "$APP_DIR/src/main.py"]
