# Optimized single-stage build with better caching
FROM python:3.12-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Set working directory
WORKDIR /usr/src/app

# Upgrade pip and configure for reliability
RUN pip install --upgrade pip && \
    pip config set global.timeout 600 && \
    pip config set global.retries 10

# Create pip cache directory for better performance
RUN mkdir -p /root/.cache/pip && \
    chown -R appuser:appgroup /root/.cache

# Copy and install core dependencies first (cacheable layer)
COPY requirements-core.txt .
RUN pip install --cache-dir /root/.cache/pip --no-cache-dir -r requirements-core.txt

# Copy and install heavy dependencies (separate layer for better caching)
COPY requirements-heavy.txt .
RUN pip install --cache-dir /root/.cache/pip --no-cache-dir -r requirements-heavy.txt

# Copy source code
COPY . .

# Set proper permissions
RUN chown -R appuser:appgroup /usr/src/app
USER appuser:appgroup

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import fastapi; print('OK')" || exit 1

CMD ["fastapi","run","main.py"]
