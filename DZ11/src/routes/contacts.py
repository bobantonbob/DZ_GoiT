from typing import List
from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.repository import contacts as repositories_contacts
from src.schemas.contact import ContactSchema, ContactUpdateSchema, ContactResponse, ContactSearchSchema
import traceback


router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.get("/", response_model=list[ContactResponse])
async def get_contacts(limit: int = Query(10, ge=10, le=500), offset: int = Query(0, ge=0),
                       db: AsyncSession = Depends(get_db)):
    contacts = await repositories_contacts.get_contacts(limit, offset, db)
    return contacts


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.create_contact(body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed to create contact")
    return contact





@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int = Path(..., ge=1), db: AsyncSession = Depends(get_db)):
    try:
        contact = await repositories_contacts.get_contact(contact_id, db)
        if not contact:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
        return contact
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put("/{contact_id}")
async def update_contact(body: ContactUpdateSchema, contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="NOT FOUND")
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.delete_contact(contact_id, db)
    return contact




@router.get("/search", response_model=List[ContactResponse])
async def search_contacts(
    first_name: str = None,
    # last_name: str = None,
    # email: str = None,
    # skip: int = 0,
    # limit: int = Query(default=10, le=100, ge=10),
    db: Session = Depends(get_db),
):
    contacts = None
    # if first_name or last_name or email:
    if first_name:
        param = {
            "first_name": first_name,
            # "last_name": last_name,
            # "email": email,
            # "skip": skip,
            # "limit": limit,
        }
        contacts = await repositories_contacts.search_contacts(param, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return contacts
