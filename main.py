import os
import uvicorn
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
version = os.getenv("VERSION")

from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from db import engine,Base,seeder,session 
from fastapi.middleware.cors import CORSMiddleware
from exception import customException
from router import auth


app = FastAPI(openapi_url="")

#Create DB schema
Base.metadata.create_all(bind=engine)
if os.getenv("SEED_MIGRATION") == 'true' :
    seeder.init_seeder()

@app.on_event("startup")
async def startup_event():
    dbConn = session()
    
#CORS config
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
    )

app.include_router(auth.router,prefix="/api/"+version)

@app.exception_handler(customException)
async def exception_handler(request: Request, exc: customException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message":exc.message},
    )
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=int(os.getenv("PORT")))
