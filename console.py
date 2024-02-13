#!/usr/bin/python3

import cmd
import json
import re
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on Ctrl-D"""
        print()
        return True

    def emptyline(self):
        """Does nothing on empty input"""
        pass

    def help_quit(self):
        """Print help message for quit command"""
        print("Quit command to exit the program.\n")

    def do_count(self, arg):
        """
            retrieves the number of instances of
            a class.
        """
        instance_count = 0
        with open("file.json", "r", encoding="utf-8") as file:
            instances = json.loads(file.read())

        list_ = arg.split()[0]
        for key in instances.keys():
            if key.split(".")[0] == list_:
                instance_count += 1
        print(instance_count)

    def validate_arg(self, args):
        """
            validate the args passed
        """
        list_ = args.split()

        if not args:
            print("** class name missing **")
            return False
            
        try:
            a = eval(list_[0])

        except NameError:
            print("** class doesn't exist **")
            return False

        if len(list_) == 1:
            print("** instance id missing **")
            return False
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        if not arg:
            print("** class name missing **")
        else:

            _list = arg.split()
            try:
                new_usr = eval(_list[0])()
                storage.save()
                print(new_usr.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string repr of an instance
            based on the class name and id
        """
        if self.validate_arg(arg):
            
            _list = arg.split()

            instance_ = "{}.{}".format(_list[0], _list[1])

            storage.reload()
            str_ = storage.all()
            try:
                print(str_[instance_])

            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name
            and id
        """
        if self.validate_arg(arg):
            list_ = arg.split()

            name = "{}.{}".format(list_[0], list_[1])
            all_ins = storage.all()
            try:
                del all_ins[name]

            except KeyError:
                print("** no instance found **")

            storage.save()

    def do_all(self, arg):
        """
            prints all string of all instances based
            or not on the class name
        """
        objects = storage.all()
        my_obj = []

        if not arg:
            for key, value in objects.items():
                my_obj.append(value.__str__())
            print(my_obj)

        else:
            class_name = arg.split()[0]
            try:
                eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return

            for key, value in objects.items():
                cls_name = key.split(".")[0]
                if cls_name == class_name:
                    my_obj.append(value.__str__())

            print(my_obj)
        
    def do_update(self, arg):
        """
            updates an instance based on the class name
            and id by adding or updating attribute
        """
        if self.validate_arg(arg):
            args_l = arg.split()
            inst_name = "{}.{}".format(args_l[0], args_l[1])
            in_dict = storage.all()

            if inst_name not in in_dict:
                print("** no instance found **")
                return

            if len(args_l) == 2:
                print("** attribute name missing **")
                return

            if len(args_l) == 3:
                print("** value missing **")
                return

            try:
                with open("file.json", "r", encoding="utf-8") as file:
                    cont_f = json.loads(file.read())
                try:
                    args_l[3] = eval(args_l[3])
                except NameError:
                    pass
                try:
                    args_l[2] = eval(args_l[2])
                except NameError:
                    pass

                cont_f[inst_name][args_l[2]] = args_l[3]

                with open("file.json", "w", encoding="utf-8") as file:
                    file.write(json.dumps(cont_f))

            except FileNotFoundError:
                pass

        else:
            return

    def get_parts(self, arg):
        """
            strips the output string using regex
            into a certain parttern
        """
        parts = re.findall(r'[\w-]+', arg)
        return parts

    def default(self, arg):
        """
        Handles command like:
            <class name>.all()
            <class.name>.count()
            <class name>.show(<id>)
            <class name>.destroy(<id>)
            <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        if arg:
            list_ = self.get_parts(arg)

            if list_:
                str_ = list_[0]

                for value in range(2, len(list_)):
                    str_ += " "
                    str_ += list_[value]

            else:
                return

            method_name = "do_" + list_[1]
            try:
                getattr(self, method_name)(str_)

            except NameError:
                print("** class doesn't exist **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
