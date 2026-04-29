# Use the official Python image.
FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

# Set working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy files
COPY . ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the web service using Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
