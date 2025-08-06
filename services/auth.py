from schema import dbSchema


async def Register(db, developer):
    try:
        new_user = dbSchema.Developer(username=developer.username, email=developer.email, password=developer.password, name=developer.name)
        db.add(new_user)
        db.commit()
        print("New user registered:", new_user)
        return new_user
    except Exception as e:
        print(e)
        return None