from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
notes = []
next_note_id =1
@app.get("/notes")
def read_notes():
    return notes

class NoteCreate(BaseModel):
    title: str
    content: str
@app.post("/notes")
def create_note(data: NoteCreate):
    global next_note_id
    note = data.model_dump()
    note["id"] = next_note_id
    notes.append(note)
    next_note_id +=1
    return note

@app.get("/notes/{note_id}")
def read_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")

