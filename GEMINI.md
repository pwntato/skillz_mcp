# GEMINI.md

## Project Overview

This project is a FastAPI server that serves as the MCP (Mission Control Plane). It is built with Python 3.11 and runs in a Docker container managed by Docker Compose. The application code is designed for hot-reloading.

## Building and Running

To build and run the server, use the following command:

```bash
docker compose up -d
```

The server will be available at [http://localhost:8000](http://localhost:8000).

## Development Conventions

*   The main application code is located in the `app` directory.
*   Python dependencies are managed in the `requirements.txt` file.
*   The `skillz` directory is mounted into the container at `/skillz` and can be used for storing and accessing data.

## Maintaining this file

This file should be kept up-to-date with any changes to the project's architecture, build process, or development conventions. When making changes to the project, please update this file accordingly.
