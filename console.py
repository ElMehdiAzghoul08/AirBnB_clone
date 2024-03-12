#!/usr/bin/python3
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

    " Method create a new instance of BaseModel and save it to JSON file"
    "and print id"
    def do_create(self, line):
        # split command line
        args = shlex.split(line)
        # check if the class name is provided
        if not args:
            print("** class name missing **")
            return
        name_of_class_ = args[0]
        if name_of_class_ not in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
        # if the class name is provided create new instance
        # and save it and print the id
        new_instance = eval(name_of_class_)()
        new_instance.save()
        print(new_instance.id)

    "Method to print the string representation*******************"
    def do_show(self, line):
        args = shlex.split(line)
        FileStorage().reload()  # reload data from the json file
        if len(args) < 1:
            print("** class name missing **")
            return
        name_of_class_ = args[0]  # class name is the first argument passed

        # Check if there are any instances of the given class
        # checking if the class exists
        if name_of_class_ not in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        # checking if the id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]  # the object id is in the second argument

        # Forming the key to search for the object in the dictionary
        objects = FileStorage().all()
        key = f"{name_of_class_}.{obj_id}"

        # getting dictionary of all objects
        all_objcts_ = FileStorage().all()
        # check if the object exist
        if key in all_objcts_:
            print(all_objcts_[key])
        else:
            print("** no instance found **")

    "Method to: Deletes an instance based on the class name and id*****"
    def do_destroy(self, line):
        args = shlex.split(line)
        FileStorage().reload()  # reload data from the jsob file
        if len(args) < 1:
            print("** class name missing **")
            return
        name_of_class_ = args[0]  # class name is first argument

        # checking if the class exist
        if name_of_class_ not in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        # checking if the id is missig
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]  # the object id is the second argument

        # forming the key to search for the object in the dictionary
        key = f"{name_of_class_}.{obj_id}"

        # get dictionary of all objects
        all_objcts_ = FileStorage().all()

        # check if the object exist

        if key in all_objcts_:
            del all_objcts_[key]  # delete the object from the dictionary
            FileStorage().save()  # save the changes to the JSON file
        else:
            print("** no instance found **")

    "Method to: Prints all string representation of all instances"
    "based or not on the class name"
    def do_all(self, line):
        args = shlex.split(line)
        FileStorage().reload()  # Reload data from the JSON file

        if len(args) == 0:
            # if class name not provided, print all instances
            all_objcts_ = FileStorage().all()
            result = [str(obj) for obj in all_objcts_.values()]
            print(result)
            return
        name_of_class_ = args[0]  # class name is the first argument

    # check if the class exists
        if name_of_class_ not in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return
    # Filter instances based on class name
        all_objcts_ = FileStorage().all()
        result = [str(obj) for key, obj in all_objcts_.items() if key.
                  startswith(name_of_class_ + ".")]
        print(result)

    "Method to : Updates an instance based on the class name"
    "and id by adding or updating attribute"
    def do_update(self, line):
        # method parses the input line into arguments using shlex.split()
        args = shlex.split(line)
        FileStorage().reload()  # Reload data from the json file

        # Check if the class name is missing
        if len(args) == 0:
            print("** class name missing **")
            return

        name_of_class_ = args[0]  # Get the class name from the arguments

        # Check if the class doesn't exit
        if name_of_class_ not in ["BaseModel", "User", "Place",
                                  "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return

        # check if the instance ID is missing
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]  # Get the object ID from thr arguments

        # Forming the key to search for the object in the dicctionary

        key = f"{name_of_class_}.{obj_id}"

        # Get the dictionnary of all objects
        all_objcts_ = FileStorage().all()

        # Check if the object exists
        if key not in all_objcts_:
            print("** no instance found **")
            return

        # Check if the attribute name is missing
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name_ = args[2]  # Get the attribute name from the arguments

        # Check if the value for the attribute name is missing
        if len(args) < 4:
            print("** value missing **")
            return

        attr_val_str_ = args[3]
        # get the attribute value as a string from the argument

        # Remove double quotes if present around the attribute value string
        if attr_val_str_[0] == '"' and attr_val_str_[-1] == '"':
            attr_val_str_ = attr_val_str_[1:-1]

        # Get the object from the dictionary using the key
        obj = all_objcts_[key]

        #  Get the attribute value type based on the attribute name
        attr_val_type_ = type(getattr(obj, attr_name_))

        # casting attribute value string to the attribute value type
        try:
            attr_value_ = attr_val_type_(attr_val_str_)
        except ValueError:
            print(f"Invalid type of attribute{attr_name_}")
            return

        # Update the objects attribute with the new value
        setattr(obj, attr_name_, attr_value_)

        # save the updated object
        FileStorage().save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
