from schema import authSchema, dbSchema
from helpers import bcryptHash, verifyBcryptHash

async def Register(db, developer):
    try:
        existing_user = db.query(dbSchema.Developer).filter_by(email=developer.email).first()
        if existing_user:
            return "exists"
        
        new_user = dbSchema.Developer(
            email=developer.email,
            password=bcryptHash(developer.password),
            name=developer.name
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return authSchema.RegisterResponse.from_orm(new_user)


    except Exception as e:
        print("Error during registration:", e)
        return None

async def Login(db, developer):
    try:
        existing_user = db.query(dbSchema.Developer).filter_by(email=developer.email).first()
        if not existing_user:
            return "not_found"

        if not verifyBcryptHash(developer.password, existing_user.password):
            return "invalid_password"
        
        return authSchema.RegisterResponse.from_orm(existing_user)

    except Exception as e:
        print("Error during login:", e)
        return None