"""
This module implements the HBNB console.
"""

import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """

    prompt = "(hbnb) "
    intro = "Welcome to the HBNB console! Type help or ? to list commands\n"

    classes = ["BaseModel"]

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the console using EOF (Ctrl-D).
        """
        return True

    def emptyline(self, line):
        """
        Do nothing when an empty line is entered.
        """
        pass
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
            return
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(lines[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
            return
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(lines) < 2:
            print("** instance id missing **")
            return
        else:
            key = lines[0] + "." + lines[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
            return
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(lines) < 2:
            print("** instance id missing **")
            return
        else:
            key = lines[0] + "." + lines[1]
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name
        """
        lines = line.split()
        if not line:
            for key, value in models.storage.all().items():
                print(value)
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            for key, value in models.storage.all().items():
                if lines[0] in key:
                    print(value)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        lines = line.split()
        if not line:
            print("** class name missing **")
            return
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(lines) < 2:
            print("** instance id missing **")
            return
        else:
            key = lines[0] + "." + lines[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            elif len(lines) < 3:
                print("** attribute name missing **")
                return
            elif len(lines) < 4:
                print("** value missing **")
                return
            else:
                setattr(models.storage.all()[key], lines[2], lines[3])
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
