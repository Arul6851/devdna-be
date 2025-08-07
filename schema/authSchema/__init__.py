from uuid import UUID
from pydantic import BaseModel as PydanticModel,ValidationError,ConfigDict
from exception import customException
from controller.http import http_codes
import datetime

class BaseModel(PydanticModel):
    def __init__(self, **data):
        try:
            super().__init__(**data)
        except ValidationError as e:
            err = e.errors()
            if err[0]['loc'][0]: # name of the Field that failed in validation
                raise customException(message=f"invalid {err[0]['loc'][0]}", status_code=400)
            raise customException(message=http_codes[400], status_code=400)
        
class Developer(BaseModel):
    email: str
    password: str
    name: str
    
class RegisterResponse(BaseModel):
    id: UUID
    email: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    
    model_config = ConfigDict(from_attributes=True)

class LoginRequest(BaseModel):
    email: str
    password: str