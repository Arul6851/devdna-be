from fastapi import APIRouter,Request,Response,Depends
from controller.http import HTTP_RESPONSE
from db import get_db
from schema import authSchema
from sqlalchemy.orm import Session
from services import auth

router = APIRouter()

@router.post("/auth")
async def Register(req:Request,res:Response,developer: authSchema.Developer,db: Session = Depends(get_db)):
    res.body = await auth.Register(db, developer)
    if res.body is None:
        return HTTP_RESPONSE(statusCode=404).returnErrorMessage(res,"Developer registration failed")
    return HTTP_RESPONSE(statusCode=200).returnCustomMessage(res, "Developer registration successful")