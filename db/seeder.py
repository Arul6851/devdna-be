from db import session
from schema import dbSchema

from sqlalchemyseed import load_entities_from_json
from sqlalchemyseed import Seeder
from sqlalchemy import select
    
def seeder(entities):
    try:
        db = session()
        new_entity  = []
        for entity in entities:
            stmt = select(dbSchema.SeedList).where(dbSchema.SeedList.id == entity['model'])
            entity_by_id = db.execute(stmt).fetchone()
            if entity_by_id == None:
                new_entity.append(entity)
                new_seed = dbSchema.SeedList(id=str(entity['model']))
                db.add(new_seed)
                
        seeder = Seeder(db)
        seeder.seed(new_entity)
        db.commit()
                
    except Exception as e:
        print(e)
        # exit(1)
                
def init_seeder():
    db_entities = load_entities_from_json('./db/data/seeder.json')
    init_entities = load_entities_from_json('./db/data/initial_seeder.json')
    seeder(init_entities)
    seeder(db_entities)    
            

            