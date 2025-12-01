FROM python:3.11.9-slim-bullseye

WORKDIR /app

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g 10001 appgroup \
    && useradd -m -u 10001 -g appgroup appuser

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /data && chown -R appuser:appgroup /data /app

EXPOSE 5000

ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    ALERTS_FILE=/data/alerts.json

USER appuser

CMD ["python", "app.py"]
