from ..middleware.database import db
import peewee
import datetime
import json

def create_db_tables():
    db.connect()
    db.create_tables([TeamcenterSystem], safe=True)

class BaseModel(peewee.Model):
    @classmethod
    def from_json(cls, json_var):
        if isinstance(json_var, dict):
            json_dict = json_var
        else:
            json_dict = json.loads(json_var)

        instance = cls(**json_dict)
        return instance

    class Meta:
        database = db

class TeamcenterSystem(BaseModel):
    system_name = peewee.CharField(
        primary_key = True, 
        unique = True,  
        max_length = 20)

    creation_date = peewee.DateTimeField(
        formats  = '%Y-%m-%d %H-%M-%S:%f', 
        default = datetime.datetime.now())
