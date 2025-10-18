# GEMINI.md

## Project Overview

This project is a FastAPI server that serves as the MCP (Mission Control Plane). It is built with Python 3.11 and runs in a Docker container managed by Docker Compose. The application code is designed for hot-reloading. It also includes a "skills" feature that allows for progressive loading of tools and functionality for an LLM.

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

### Skills

The `skillz` directory contains a collection of skills that can be progressively loaded and used by an LLM. Each skill is a directory that contains a `SKILL.md` file with YAML front matter for the `name` and `description` of the skill. The `SKILL.md` file can then reference other files within the skill's directory.

To create a new skill:
1.  Create a new directory in the `skillz` directory.
2.  Create a `SKILL.md` file in the new directory with YAML front matter for `name` and `description`.
3.  Add any other files for the skill in the same directory and reference them in the `SKILL.md` file.
*   New skill folders added to the `skillz` directory will be ignored by Git, except for `skillz/sample_skill/`.

## Maintaining this file

This file should be kept up-to-date with any changes to the project's architecture, build process, or development conventions. When making changes to the project, please update this file accordingly.
