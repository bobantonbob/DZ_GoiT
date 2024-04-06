import fastapi
import fastapi
import database

import planes.models as models
import planes.schemas as schemas

router = fastapi.APIRouter(prefix='/planes', tags=["planes"])

@router.get("/")
async def root(
    db=fastapi.Depends(database.get_database)
) -> list[schemas.PlaneResponseSchema]:
    return [plane for plane in db.query(models.PlaneModel).all()]


@router.get("/err")
async def test_err_route():
    raise fastapi.HTTPException(503, "Test error")
