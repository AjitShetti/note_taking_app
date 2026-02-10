from sqlalchemy.orm import Session
from . import models, schemas

# 1. READ (Get a single note)
def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# 2. READ (Get all notes)
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

# 3. CREATE
def create_note(db: Session, note: schemas.NoteCreate):
    # Convert Pydantic model to SQLAlchemy model
    # **note.dict() unpacks the dictionary: title="...", content="..."
    db_note = models.Note(**note.dict()) 
    db.add(db_note)
    db.commit()
    db.refresh(db_note) # Refresh to get the new ID back
    return db_note

# 4. DELETE
def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
        return True
    return False

# 5. UPDATE
def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if not db_note:
        return None
    
    # Update only the fields that are sent
    note_data = note.dict(exclude_unset=True)
    for key, value in note_data.items():
        setattr(db_note, key, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note