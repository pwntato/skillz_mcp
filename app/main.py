from fastapi import FastAPI, HTTPException
import os
import frontmatter
from pathlib import Path
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.get("/skills")
def list_skills():
    skills_dir = Path(os.getenv("SKILLZ_DIR", "/skillz"))
    if not skills_dir.is_dir():
        return {"error": "skillz directory not found"}

    skills = []
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir():
            skill_file_path = skill_dir / "SKILL.md"
            if skill_file_path.is_file():
                try:
                    post = frontmatter.load(skill_file_path)
                    skills.append({
                        "name": post.get("name"),
                        "description": post.get("description"),
                        "skill_id": skill_dir.name
                    })
                except Exception as e:
                    # Ignore files that don't have valid frontmatter
                    pass
    return {"skills": skills}

@app.get("/skills/{skill_id}")
def get_skill(skill_id: str):
    skill_dir = Path(os.getenv("SKILLZ_DIR", "/skillz")) / skill_id
    if not skill_dir.is_dir():
        raise HTTPException(status_code=404, detail="Skill not found")

    skill_file_path = skill_dir / "SKILL.md"
    if not skill_file_path.is_file():
        raise HTTPException(status_code=404, detail="SKILL.md not found")

    with open(skill_file_path, "r") as f:
        post = frontmatter.load(f)

    files = []
    for dirpath, _, filenames in os.walk(skill_dir):
        for filename in filenames:
            relative_path = Path(dirpath).relative_to(skill_dir) / filename
            files.append(str(relative_path))
    
    return {"content": post.content, "metadata": post.metadata, "files": files}

@app.get("/skills/{skill_id}/files")
def list_skill_files(skill_id: str):
    skill_dir = Path(os.getenv("SKILLZ_DIR", "/skillz")) / skill_id
    if not skill_dir.is_dir():
        raise HTTPException(status_code=404, detail="Skill not found")

    files = []
    for dirpath, _, filenames in os.walk(skill_dir):
        for filename in filenames:
            relative_path = Path(dirpath).relative_to(skill_dir) / filename
            files.append(str(relative_path))

    return {"files": files}

@app.get("/skills/{skill_id}/{file_path:path}")
def get_skill_file(skill_id: str, file_path: str):
    skill_dir = Path(os.getenv("SKILLZ_DIR", "/skillz")) / skill_id
    if not skill_dir.is_dir():
        raise HTTPException(status_code=404, detail="Skill not found")

    file = skill_dir / file_path
    if not file.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    with open(file, "r") as f:
        post = frontmatter.load(f)
        return {"content": post.content, "metadata": post.metadata}