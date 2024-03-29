import fastapi
import database

import contacts.schemas as schemas
import contacts.models as models

router = fastapi.APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/")
async def root(
        db=fastapi.Depends(database.get_database)
) -> list[schemas.ContactResponseSchema]:
    return [contact for contact in db.query(models.ContactModel).all()]


