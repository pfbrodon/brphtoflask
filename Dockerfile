FROM python:3.12.2-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers python3-dev

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

#CMD ["python", "app.py"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
