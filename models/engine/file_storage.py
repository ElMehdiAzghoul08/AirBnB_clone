import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    #path to JSON file
    __file_path = "file.json"
    #a dictionary to store objects
    __objects = {}
    classes = { 
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    } #add attribute to store registered classes

    def all(self):
        #return the dictionary of all objects
        return self.__objects

    def new(self, obj):
        #adds new object to dictionary
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        #serialize __object to JSON and save it to the file
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file, indent=4)

    def reload(self):
        #Deserialize JSON from the file and update __objects
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    if class_name not in self.classes:
                        self.classes[class_name] = eval(class_name)
                    self.__objects[key] = self.classes[class_name](**value)

        except FileNotFoundError:
            pass