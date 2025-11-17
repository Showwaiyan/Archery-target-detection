# Run Python Image
FROM python:3.12-bullseye

# Get System update
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Create user and set to only working dir priviledge
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set Working DIR
WORKDIR /usr/src/app

# COPY Requirement Dep
COPY requirements.txt .

# Install Dep
RUN pip install --no-cache-dir -r requirements.txt

# COPY source code
COPY . .

# Set non-root user
RUN chown -R appuser:appgroup /usr/src/app
USER appuser:appgroup

# RUN python file
CMD ["fastapi","run"]
