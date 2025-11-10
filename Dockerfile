# 1) Use a specific lightweight Python base image (pin to 3.11.9)
FROM python:3.11.9-slim

# 2) Set working directory inside the container
WORKDIR /app

# 3) Install OS updates and create non-root user/group
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/* \
  && groupadd -g 10001 appgroup \
  && useradd -m -u 10001 -g appgroup appuser

# 4) Copy dependency list first for better caching
COPY requirements.txt .

# 5) Install Python dependencies
RUN python -m pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# 6) Copy the rest of the application source code
COPY . .

# 7) Prepare writable data directory and adjust permissions
RUN mkdir -p /data && chown -R appuser:appgroup /data /app

# 8) Expose Flask port
EXPOSE 5000

# 9) Set environment defaults (can be overridden at runtime)
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    ALERTS_FILE=/data/alerts.json

# 10) Switch to non-root user for security
USER appuser

# 11) Run the application
CMD ["python", "app.py"]
