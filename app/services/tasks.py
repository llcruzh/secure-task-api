from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.task import Task

def create_task(db: Session, owner_id: int, title: str, description: str, status: str, priority: int) -> Task:
    t = Task(owner_id=owner_id, title=title, description=description, status=status, priority=priority)
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

def list_tasks(db: Session, owner_id: int) -> list[Task]:
    return list(db.execute(select(Task).where(Task.owner_id == owner_id).order_by(Task.id.desc())).scalars())

def get_task(db: Session, owner_id: int, task_id: int) -> Task | None:
    return db.execute(select(Task).where(Task.owner_id == owner_id, Task.id == task_id)).scalar_one_or_none()

def update_task(db: Session, task: Task, **updates) -> Task:
    for k, v in updates.items():
        if v is not None:
            setattr(task, k, v)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()
