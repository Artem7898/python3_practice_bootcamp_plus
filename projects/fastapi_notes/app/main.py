from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Notes API")
DB: Dict[int, str] = {}
SEQ = 0

class NoteIn(BaseModel):
    text: str

class NoteOut(BaseModel):
    id: int
    text: str

@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn):
    global SEQ
    SEQ += 1
    DB[SEQ] = note.text
    return NoteOut(id=SEQ, text=note.text)

@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int):
    if note_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    return NoteOut(id=note_id, text=DB[note_id])

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id not in DB:
        raise HTTPException(status_code=404, detail="Not found")
    del DB[note_id]
    return {"ok": True}
