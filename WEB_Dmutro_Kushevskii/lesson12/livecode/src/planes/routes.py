import fastapi
import database

import auth.service
import planes.models as models
import planes.schemas as schemas

router = fastapi.APIRouter(prefix='/planes', tags=["planes"])
auth_service = auth.service.Auth()

@router.get("/")
async def root(
    db=fastapi.Depends(database.get_database),
    user = fastapi.Depends(auth_service.get_user),
) -> list[schemas.PlaneResponseSchema]:
    return [
        plane
        for plane in db.query(models.PlaneModel).filter(
            models.PlaneModel.user_id==user.id
        ).all()
    ]


@router.get("/err")
async def test_err_route():
    raise fastapi.HTTPException(503, "Test error")
