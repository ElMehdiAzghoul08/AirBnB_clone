import cmd
import shlex



class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)"
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
