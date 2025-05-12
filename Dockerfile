FROM python:3.8-slim-buster

# Install required system dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the application code
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python3", "app.py"]
