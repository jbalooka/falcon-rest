from ..middleware.database import db
import peewee
import datetime

class BaseModel(peewee.Model):
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

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
