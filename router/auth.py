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
    if res.body == "exists":
        return HTTP_RESPONSE(statusCode=409).returnErrorMessage(res, "Developer already exists")
    if res.body is None:
        return HTTP_RESPONSE(statusCode=500).returnErrorMessage(res,"Internal Server Error during registration")
    return HTTP_RESPONSE(statusCode=200).returnCustomMessage(res, "Developer registration successful")

@router.post("/auth/login")
async def Login(req:Request,res:Response,developer: authSchema.LoginRequest,db: Session = Depends(get_db)):
    res.body = await auth.Login(db, developer)
    if res.body == "not_found":
        return HTTP_RESPONSE(statusCode=404).returnErrorMessage(res, "Developer not found")
    if res.body == "invalid_password":
        return HTTP_RESPONSE(statusCode=401).returnErrorMessage(res, "Authentication failed, invalid password")
    if res.body is None:
        return HTTP_RESPONSE(statusCode=500).returnErrorMessage(res,"Internal Server Error during login")
    return HTTP_RESPONSE(statusCode=200).returnCustomMessage(res, "Login successful")