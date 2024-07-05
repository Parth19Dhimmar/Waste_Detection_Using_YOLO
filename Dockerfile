# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3-opencv ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /tmp/*

# Copy the rest of the application code
COPY . /app/

# Command to run the application
CMD ["python", "app.py"]
