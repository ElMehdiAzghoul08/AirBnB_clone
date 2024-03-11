import cmd
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        from models.engine.file_storage import FileStorage
        # initializing BaseModel instance
        # datetime object format
        objct_formatt_ = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.
                                strptime(value, objct_formatt_))
                    else:
                        setattr(self, key, value)
        else:
            # create id and created_at and updated_at
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.first_name = ""  # Add the first_name attribute
            # adding new object to storage
            FileStorage().new(self)

    def __str__(self):
        # Return string representation
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models.engine.file_storage import FileStorage
        # update updated_at and save to storage
        self.updated_at = datetime.now()
        FileStorage().save()

    def to_dict(self):
        # creating a dictionary that contains all key/values of the instances
        dictionary_instances_ = self.__dict__.copy()
        # add a key __class__ in the object class name
        dictionary_instances_['__class__'] = self.__class__.__name__
        dictionary_instances_['created_at'] = self.created_at.isoformat()
        dictionary_instances_['updated_at'] = self.updated_at.isoformat()
        return dictionary_instances_
