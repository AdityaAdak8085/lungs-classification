FROM python:3.8-slim-buster

# Install all OpenCV system-level dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install the latest version of TensorFlow
RUN pip install --upgrade tensorflow

WORKDIR /app

# Copy code into the Docker container
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run your application
CMD ["python3", "app.py"]
