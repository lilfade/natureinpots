FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    apt-get clean

# Copy everything into container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make init script executable
RUN chmod +x /app/init_db.sh

# Expose Flask port
EXPOSE 5000
