FROM python:3.8-slim-buster

# Install OpenCV and system dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Install dependencies, force TensorFlow 2.15 to fix TFLite ops
RUN pip install --no-cache-dir tensorflow==2.15.0 \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
