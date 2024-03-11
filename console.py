"""console Module"""
import cmd
import shlex
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)"
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    
    " Method to create a new instance of BaseModel and save it to JSON file and print the id**********************************************"
    def do_create(self, line):
        #split command line
        args = shlex.split(line)
        #check if the class name is provided
        if not args:
            print("** class name is missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        #if the class name is provided create new instance
        #and save it and print the id
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    "Method to print the string representation*******************************************************************************************"
    def do_show(self, line):
        args = shlex.split(line)
        FileStorage().reload() #reload data from the json file
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0] #class name is the first argument passed

        # Check if there are any instances of the given class
        #checking if the class exists
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
            
        #checking if the id is missing
        if len(args) < 2:
            print("** instance id is missing **")
            return
            
        obj_id = args[1] #the object id is in the second argument
        
        #Forming the key to search for the object in the dictionary
        objects = FileStorage().all()
        key = f"{class_name}.{obj_id}"
    
        #getting dictionary of all objects
        all_objects = FileStorage().all()

         #check if the object exist
        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")
    

    "Method to: Deletes an instance based on the class name and id*****************************************************************"
    def do_destroy(self, line):
        args = shlex.split(line)
        FileStorage().reload() #reload data from the jsob file
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0] #class name is first argument

        #checking if the class exist
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        
        #checking if the id is missig
        if len(args) < 2:
            print("** instance id is missing **")
            return
        
        obj_id = args[1] #the object id is the second argument

        #forming the key to search for the object in the dictionary
        key = f"{class_name}.{obj_id}"

        #get dictionary of all objects
        all_objects = FileStorage().all()

        #check if the object exist

        if key in all_objects:
            del all_objects[key] # delete the object from the dictionary
            FileStorage().save() #save the changes to the JSON file
        else:
            print("** no instance found **")



    "Method to: Prints all string representation of all instances based or not on the class name****************************************"
    def do_all(self, line):
        args = shlex.split(line)
        FileStorage().reload() #Reload data from the JSON file

        if len(args) == 0 :
        #if class name not provided, print all instances
            all_objects = FileStorage().all()
            result = [str(obj) for obj in all_objects.values()]
            print(result)
            return
        class_name = args[0] #class name is the first argument

    #check if the class exists
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
    #Filter instances based on class name
        all_objects = FileStorage().all()
        result = [str(obj) for key, obj in all_objects.items() if key.startswith(class_name + ".")]
        print(result)


    "Method to : Updates an instance based on the class name and id by adding or updating attribute**************************************"
    def do_update(self, line):
        #The do_update method parses the input line into arguments using shlex.split()
        args = shlex.split(line)
        FileStorage().reload() #Reload data from the json file

        #Check if the class name is missing
        if len(args) == 0:
            print("** class name missing **")
            return
        
        class_name = args[0] #Get the class name from the arguments

        #Check if the class doesn't exit
        if class_name not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        

        #check if the instance ID is missing
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        obj_id = args[1] #Get the object ID from thr arguments

        #Forming the key to search for the object in the dicctionary
        
        key = f"{class_name}.{obj_id}"

        #Get the dictionnary of all objects
        all_objects = FileStorage().all()

        #Check if the object exists
        if key not in all_objects:
            print("** no instance found **")
            return
        
        #Check if the attribute name is missing
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2] #Get the attribute name from the arguments

        #Check if the value for the attribute name is missing
        if len(args) < 4:
            print("** value missing **")
            return
        
        attribute_value_str = args[3] #get the attribute value as a string from the argument

        #Remove double quotes if present around the attribute value string
        if attribute_value_str[0] == '"' and attribute_value_str[-1] == '"':
            attribute_value_str = attribute_value_str[1:-1]

        #Get the object from the dictionary using the key
        obj = all_objects[key]

        #Get the attribute value type based on the attribute name
        attribute_value_type = type(getattr(obj, attribute_name))

        # casting attribute value string to the attribute value type
        try:
            attribute_value = attribute_value_type(attribute_value_str)
        except ValueError:
            print(f"Invalid type of attribute{attribute_name}")
            return
        
        #Update the objects attribute with the new value
        setattr(obj, attribute_name, attribute_value)

        #save the updated object
        FileStorage().save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()