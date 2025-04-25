FROM --platform=linux/amd64 python:3.10-slim

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
    PYSPARK_PYTHON=python3

# Install Java 17 and minimal OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk-headless \
    curl \
    build-essential \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create data directories
RUN mkdir -p /app/data/input /app/data/output/

# Install uv
RUN pip install uv

# Copy pyproject.toml and install dependencies with uv
COPY pyproject.toml .
RUN uv pip install --system -e .

# Copy application code
COPY src/ src/
COPY . .

# Default command to run your script
CMD ["python", "-m", "src.main"]
