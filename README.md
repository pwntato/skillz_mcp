# Mission Control Plane (MCP) Server

## Project Overview

This project implements a Mission Control Plane (MCP) server using FastAPI, designed to provide a robust and extensible backend for managing and interacting with various functionalities, referred to as "skills." It leverages Docker and Docker Compose for easy deployment and includes hot-reloading for efficient development.

## Features

*   **FastAPI Backend:** A high-performance, easy-to-use web framework for building APIs with Python 3.11.
*   **Dockerized Deployment:** Packaged in a `python:3.11-slim` Docker container for consistent environments.
*   **Docker Compose:** Simplifies the management and orchestration of the server and its dependencies.
*   **Hot-Reloading:** Automatic code reloading during development for a smooth workflow.
*   **Skills Feature:** A dynamic system allowing LLMs to progressively discover and utilize tools/functionalities defined in a structured `skillz` directory.

## Getting Started

To set up and run the MCP server, ensure you have Docker and Docker Compose installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pwntato/skillz_mcp
    cd skillz_mcp
    ```

2.  **Start the server:**
    ```bash
    docker compose up -d
    ```

    This command will build the Docker image (if not already built) and start the server in detached mode.

3.  **Access the API Documentation:**
    The server will be available at `http://localhost:8000`. You can access the interactive API documentation (Swagger UI) by navigating to `http://localhost:8000/docs` in your web browser.

## API Endpoints

*   `/`: Redirects to the API documentation (`/docs`).
*   `/skills`: Returns a list of available skills, including their name, description, and `skill_id` (derived from the skill's directory name).
*   `/skills/{skill_id}/{file_path:path}`: Retrieves the content of a specific file within a given skill's directory. This is used by LLMs for progressive loading of skill details and associated scripts.

## Skills Development

The "skills" feature allows for dynamic extension of the MCP server's capabilities. Each skill is defined within its own directory under the `skillz/` folder.

To create a new skill, refer to the detailed instructions in `GEMINI.md` under the "Development Conventions" section.

## Testing

Automated tests are configured using `pytest` and can be run locally or via GitHub Actions.

To run tests locally (ensure you have `pytest` and `httpx` installed in your local Python environment):

```bash
PYTHONPATH=. pytest
```

## Contributing

Contributions are welcome! Please refer to `GEMINI.md` for development conventions and guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
