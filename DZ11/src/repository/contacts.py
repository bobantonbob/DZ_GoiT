from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.entity.models import Contact
from src.schemas.contact import ContactSchema, ContactUpdateSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    stmt = select(Contact).offset(offset).limit(limit)
    contacts = await db.execute(stmt)
    return contacts.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdateSchema, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    result = await db.execute(stmt)
    contact = result.scalar_one_or_none()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birthday = body.birthday
        contact.extra_info = body.extra_info
        await db.commit()
        await db.refresh(contact)
    return contact


async def delete_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contact).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    contact = contact.scalar_one_or_none()
    if contact:
        await db.delete(contact)
        await db.commit()
    return contact



async def search_contacts(param: dict, db: Session):
    query = db.query(Contact)
    first_name = param.get("first_name")
    # last_name = param.get("last_name")
    # email = param.get("email")
    if first_name:
        query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
    # if last_name:
    #     query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))
    # if email:
    #     query = query.filter(Contact.email.ilike(f"%{email}%"))
    contacts = query.offset(param.get("skip")).limit(param.get("limit"))
    return contacts



