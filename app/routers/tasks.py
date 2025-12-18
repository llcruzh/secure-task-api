from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import decode_token
from app.schemas.task import TaskCreate, TaskOut, TaskUpdate
from app.services.tasks import create_task, list_tasks, get_task, update_task, delete_task

router = APIRouter(prefix="/tasks", tags=["tasks"])
auth_scheme = HTTPBearer()

def get_current_user_id(creds: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> int:
    token = creds.credentials
    user_id = decode_token(token)
    return int(user_id)

@router.get("", response_model=list[TaskOut])
def tasks(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return list_tasks(db, user_id)

@router.post("", response_model=TaskOut, status_code=201)
def create(payload: TaskCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return create_task(db, user_id, payload.title, payload.description, payload.status, payload.priority)

@router.get("/{task_id}", response_model=TaskOut)
def read(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    t = get_task(db, user_id, task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.patch("/{task_id}", response_model=TaskOut)
def patch(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    t = get_task(db, user_id, task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return update_task(db, t, title=payload.title, description=payload.description, status=payload.status, priority=payload.priority)

@router.delete("/{task_id}", status_code=204)
def remove(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    t = get_task(db, user_id, task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, t)
    return None
