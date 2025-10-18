import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
import shutil
from pathlib import Path

@pytest.fixture(name="client")
def client_fixture(skillz_test_dir):
    # Set the SKILLZ_DIR environment variable for the test client
    os.environ["SKILLZ_DIR"] = str(skillz_test_dir)
    with TestClient(app) as client:
        yield client
    del os.environ["SKILLZ_DIR"]

@pytest.fixture(name="skillz_test_dir")
def skillz_test_dir_fixture(tmp_path):
    # Create a temporary directory for skillz
    temp_skillz_dir = tmp_path / "skillz_test"
    temp_skillz_dir.mkdir()

    # Copy the sample_skill into the temporary directory
    shutil.copytree("skillz/sample_skill", temp_skillz_dir / "sample_skill")

    yield temp_skillz_dir

    # Clean up the temporary directory
    shutil.rmtree(temp_skillz_dir)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_list_skills(client):
    response = client.get("/skills")
    assert response.status_code == 200
    assert "skills" in response.json()
    assert len(response.json()["skills"]) > 0
    assert response.json()["skills"][0]["skill_id"] == "sample_skill"

def test_get_skill_file(client):
    response = client.get("/skills/sample_skill/SKILL.md")
    assert response.status_code == 200
    assert "content" in response.json()
    assert "# Sample Skill" in response.json()["content"]

def test_get_non_existent_skill_file(client):
    response = client.get("/skills/sample_skill/non_existent_file.txt")
    assert response.status_code == 404
    assert response.json() == {"detail": "File not found"}

def test_get_non_existent_skill(client):
    response = client.get("/skills/non_existent_skill/SKILL.md")
    assert response.status_code == 404
    assert response.json() == {"detail": "Skill not found"}