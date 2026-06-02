# ── Stage 1: base image ──────────────────────────────────────────
FROM python:3.11-slim

# Metadata
LABEL maintainer="codearts-demo"
LABEL description="Task Manager API - CodeArts Demo Project"
LABEL version="1.0.0"

# Set working directory
WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the application
CMD ["python", "main.py"]
