from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import contacts as repositories_contact
from src.schemas.contact import ContactSchema, ContactUpdateSchema, ContactResponse

router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get("/", response_model=list[ContactResponse])
async def get_contacts(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                       db: AsyncSession = Depends(get_db)):
    contacts = await repositories_contact.get_contacts(limit, offset, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contact.get_contacts(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: AsyncSession = Depends(get_db)):
    contact = await repositories_contact.create_contact(body, db)
    return contact


@router.put("/{contact_id}")
async def update_contact(body: ContactUpdateSchema, contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contact.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contact.delete_contact(contact_id, db)
    return contact

# from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from src.database.db import get_db
# from src.repository import todos as repositories_todos
# from src.schemas.todo import TodoSchema, TodoUpdateSchema, TodoResponse
#
# router = APIRouter(prefix='/todos', tags=['todos'])
#
#
# @router.get("/", response_model=list[TodoResponse])
# async def get_todos(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
#                     db: AsyncSession = Depends(get_db)):
#     todos = await repositories_todos.get_todos(limit, offset, db)
#     return todos
#
#
# @router.get("/{todo_id}", response_model=TodoResponse)
# async def get_todo(todo_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
#     todo = await repositories_todos.get_todo(todo_id, db)
#     if todo is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
#     return todo
#
#
# @router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
# async def create_todo(body: TodoSchema, db: AsyncSession = Depends(get_db)):
#     todo = await repositories_todos.create_todo(body, db)
#     return todo
#
#
# @router.put("/{todo_id}")
# async def update_todo(body: TodoUpdateSchema, todo_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
#     todo = await repositories_todos.update_todo(todo_id, body, db)
#     if todo is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
#     return todo
#
#
# @router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(todo_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
#     todo = await repositories_todos.delete_todo(todo_id, db)
#     return todo
