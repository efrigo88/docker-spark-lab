# Docker Spark Lab

A Python project with Apache Spark integration, containerized using Docker.

## Prerequisites

- Docker
- Docker Compose
- Python 3.10 (if running locally)

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd docker-spark-lab
```

2. Create data directories:

```bash
mkdir -p data/input data/output
```

3. Source the environment variables and modify if needed:

```bash
# Source the .env file
source .env

# Optional: Modify Spark configuration if needed
# export THREADS="local[8]"
# export DRIVER_MEMORY="16g"
# export SHUFFLE_PARTITIONS="8"
```

4. Run using Docker Compose:

```bash
docker-compose up -d --build
```

5. Execute the Spark job:

```bash
docker exec -it docker-spark-lab-spark-lab-1 python -m src.main
```

6. Clean up (stop containers and remove volumes):

```bash
docker-compose down -v
```

Alternatively, you can use Docker commands directly:

```bash
docker build -t spark-lab .
docker run -v $(pwd)/data:/app/data spark-lab python -m src.main
```

## Project Structure

```
docker-spark-lab/
├── data/                   # Data directory (mounted as volume)
│   ├── input/             # Input files (e.g., JSON)
│   └── output/            # Output files (e.g., Delta tables)
├── src/                   # Source code
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Main application entry point
│   └── helpers.py        # Spark session and schema definitions
├── Dockerfile            # Container configuration
├── docker-compose.yml    # Docker Compose configuration
├── .env                  # Environment variables for Spark configuration
└── pyproject.toml        # Python project dependencies
```

## Environment Variables

The project uses environment variables for Spark configuration:

- `THREADS`: Number of threads for Spark local mode (e.g., "local[4]")
- `DRIVER_MEMORY`: Memory allocation for Spark driver (e.g., "8g")
- `SHUFFLE_PARTITIONS`: Number of partitions for shuffle operations (e.g., "4")

These variables are automatically loaded by Docker Compose from the `.env` file.

## Development

The project uses:

- Python 3.10
- Apache Spark
- Java 17
- UV for Python package management
- Delta Lake for data storage

Docker Compose Bake optimization can be enabled by setting the `COMPOSE_BAKE` environment variable in your shell:

```bash
export COMPOSE_BAKE=true
```

This feature improves build performance by delegating builds to Bake, which can cache build steps more efficiently and parallelize the build process. Note that this is a host-side configuration and should be set in your shell environment, not in the container.

## Inspecting Data Files

After running the container, you can inspect the generated files:

```bash
# List Delta table files
ls -la data/output/delta_table/

# Enter the container shell
docker exec -it docker-spark-lab-spark-lab-1 bash

# Run Python REPL in container
docker exec -it docker-spark-lab-spark-lab-1 python
```

## License

[Add your license information here]
