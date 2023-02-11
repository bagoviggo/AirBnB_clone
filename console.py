#!/usr/bin/python3
# console.py

"""Entry point for the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Inherits from the cmd module and defines methods to
    initialize commands for the interpreter"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Exiting the program cleanly"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Empty line + ENTER should not execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
