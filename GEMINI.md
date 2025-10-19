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

## API Endpoints

The following endpoints are available:

*   `GET /`: Redirects to the FastAPI documentation.
*   `GET /skills`: Lists all available skills.
*   `GET /skills/{skill_id}`: Returns the content of the `SKILL.md` file for the specified skill.
*   `GET /skills/{skill_id}/{file_path}`: Returns the content of a specific file for the specified skill.
*   `GET /skills/{skill_id}/files`: Returns a list of all files for the specified skill.

## Using Skills Locally

The MCP server exposes skills, allowing clients to retrieve skill definitions and associated files for local execution. This enables flexible use of skills in various environments.

To use a skill locally:

1.  **Identify the Skill**: Use the `GET /skills` endpoint to list available skills and their `skill_id`.

    ```bash
    curl http://localhost:8000/skills
    ```

2.  **Retrieve Skill Files**: You can retrieve individual skill files using `GET /skills/{skill_id}/{file_path}`. For example, to get the `SKILL.md` for `slack-gif-creator`:

    ```bash
    curl http://localhost:8000/skills/slack-gif-creator/SKILL.md
    ```

    To get a list of all files within a skill, use `GET /skills/{skill_id}/files`:

    ```bash
    curl http://localhost:8000/skills/slack-gif-creator/files
    ```

    You can then iterate through the file list and download each file, recreating the skill's directory structure locally.

3.  **Install Dependencies**: Refer to the skill's `SKILL.md` for any specific dependencies. For Python-based skills, these are typically installed via `pip`. For example, the `slack-gif-creator` skill requires:

    ```bash
    pip install pillow imageio numpy
    ```

4.  **Execute the Skill Locally**: Once the skill files are downloaded and dependencies are installed, you can execute the skill's logic in your local environment. Refer to the skill's documentation (e.g., `SKILL.md` or other files) for usage examples and entry points.

    For instance, to run a Python script from a downloaded skill, you would navigate to the skill's directory and execute the script:

    ```bash
    python your_skill_script.py
    ```



## Maintaining this file

This file should be kept up-to-date with any changes to the project's architecture, build process, or development conventions. When making changes to the project, please update this file accordingly.
*   The `README.md` file should always be kept up-to-date with the latest project information, features, and instructions.
