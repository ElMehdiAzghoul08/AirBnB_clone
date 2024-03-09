import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        #datetime object format
        obj_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, obj_format))
                    else:
                        setattr(self, key, value)
        else:
                #create id and created_at and updated_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # adding new object to storage
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        #update updated_at and save to storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        #creating a dictionary that contains all key/values of the instances
        dict_instance = self.__dict__.copy()
        # add a key __class__ in the object class name
        dict_instance['__class__'] = self.__class__.__name__
        dict_instance['created_at'] = self.created_at.isoformat()
        dict_instance['updated_at'] = self.updated_at.isoformat()
        return dict_instance
    