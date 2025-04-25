# Docker Spark Lab

A Python project with Apache Spark integration, containerized using Docker.

## Prerequisites

- Docker
- Python 3.10 (if running locally)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd docker-spark-lab
```

2. Build the Docker image:
```bash
docker build -t spark-lab .
```

3. Run the container:
```bash
docker run spark-lab
```

## Project Structure

- `main.py`: Main application entry point
- `Dockerfile`: Container configuration
- `pyproject.toml`: Python project dependencies

## Development

The project uses:
- Python 3.10
- Apache Spark
- Java 17
- UV for Python package management

## License

[Add your license information here] 