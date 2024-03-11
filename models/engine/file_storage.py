"""doc"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    # path to JSON file
    __file_path = "file.json"
    # a dictionary to store objects
    __objects = {}
    classes__ = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }  # add attribute to store registered classes__

    def all(self):
        # return the dictionary of all objects
        return self.__objects

    def new(self, obj):
        # adds new object to dictionary
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        # serialize __object to JSON and save it to the file
        object_dictionary_ = {key: obj.
                              to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(object_dictionary_, file, indent=4)

    def reload(self):
        # Deserialize JSON from the file and update __objects
        try:
            with open(self.__file_path, 'r') as file:
                object_dictionary_ = json.load(file)
                for key, value in object_dictionary_.items():
                    name_of_class_ = key.split('.')[0]
                    if name_of_class_ not in self.classes__:
                        self.classes__[name_of_class_] = eval(name_of_class_)
                    self.__objects[key] = self.classes__[
                        name_of_class_](**value)

        except FileNotFoundError:
            pass
