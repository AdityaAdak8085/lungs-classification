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

WORKDIR /app

# Copy code and install Python dependencies
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
