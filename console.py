#!/usr/bin/python3
"""cmd module to make command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """class commands"""

    prompt = "(hbnb) "
    list_of_classes = ["BaseModel", "User",
                       "City", "State", "Amenity", "Review", "Place"]

    def do_EOF(self, line):
        """EOF command to exit the program"""

        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def emptyline(self):
        """emptyline command to execute anything"""

        pass

    def do_create(self, line):
        """Creates a new instance"""

        if line:
            if line not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                instance = eval(f"{line}()")
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of \
            an instance based on the class name and id"""

        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        print(value)
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""

        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        del dic[key]
                        storage.save()
                        flag = 1
                        break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all\
            instances based or not on the class name"""

        new_list = []
        dic = storage.all()
        for value in dic.values():
            new_list.append(str(value))
        if line:
            if line not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            else:
                print(new_list)
        else:
            print(new_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        list_line = line.split(" ")
        if line:
            list_line = line.split(" ")
            if list_line[0] not in HBNBCommand.list_of_classes:
                print("** class doesn't exist **")
            elif len(list_line) == 1:
                print("** instance id missing **")
            elif list_line[1]:
                dic = storage.all()
                flag = 0
                for key, value in dic.items():
                    if f"{list_line[0]}.{list_line[1]}" == key:
                        if len(list_line) == 2:
                            print("** attribute name missing **")
                            flag = 1
                        elif len(list_line) == 3:
                            print("** value missing **")
                            flag = 1
                        else:
                            setattr(value, list_line[2], (list_line[3])[1: -1])
                            storage.save()
                            flag = 1
                            break
                if flag == 0:
                    print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
