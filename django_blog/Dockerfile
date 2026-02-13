# 1. Base Image: Use a lightweight Python version
FROM python:3.10-slim

# 2. Set Environment Variables
# Prevents Python from writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures console output is flushed directly to terminal (no buffering)
ENV PYTHONUNBUFFERED 1

# 3. Set Work Directory
WORKDIR /app

# 4. Install System Dependencies
# These are required to build the mysqlclient library
RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Install Python Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy Project Code
COPY . /app/

# 7. Expose Port
EXPOSE 8000

# 8. Run Command
# Start the server accessible from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
