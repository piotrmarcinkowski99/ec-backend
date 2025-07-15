import uuid
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.schemas.task_schemas import TaskSchema

router = APIRouter()

import uuid

task_list = [
    {
        "id": str(uuid.uuid4()),
        "title": "Przygotowanie raportu miesięcznego",
        "description": "Sporządź szczegółowy raport za ostatni miesiąc i prześlij do zespołu finansowego.",
        "completed": False,
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Spotkanie z klientem – Nowy Projekt",
        "description": "Omów zakres współpracy i wymagania funkcjonalne dla projektu aplikacji mobilnej.",
        "completed": True,
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Aktualizacja dokumentacji technicznej",
        "description": "Zaktualizuj README oraz dokumentację API po ostatnich wdrożeniach.",
        "completed": False,
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Code review – moduł logowania",
        "description": "Sprawdź poprawność implementacji logiki logowania i autoryzacji.",
        "completed": True,
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Testy końcowe wersji 2.3",
        "description": "Wykonaj testy regresji przed publikacją nowej wersji aplikacji.",
        "completed": False,
    },
]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def fint_task_by_id(task_id: str):  
    for task in task_list:
        print(task)
        print('________')
    return next(filter(lambda t: t["id"] == task_id, task_list), None)

@router.post("")
async def add_task(task: TaskSchema):
    task_dict = task.model_dump()
    task_dict["id"] = str(task.id)
    task_list.append(task_dict)
    return {"message": "Task added successfully", "task": task}

@router.get("")
async def get_all_tasks():
    return task_list

@router.put("/{task_id}")
async def update_task(task_id: str, task: TaskSchema):
    task_to_update = fint_task_by_id(task_id)

    if task_to_update is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_to_update["title"] = task.title
    task_to_update["description"] = task.description
    task_to_update["completed"] = task.completed

    return {"message": "Task updated successfully", "task": task_to_update}

@router.delete("/{task_id}")
async def delete_task(task_id: str):
    task_to_delete = fint_task_by_id(task_id)

    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")

    task_list.remove(task_to_delete)

    return {"message": "Task deleted successfully"}
