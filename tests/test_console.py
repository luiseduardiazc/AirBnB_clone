#!/usr/bin/python3
''' Test for class HBNBCommand '''
import unittest
from unittest import mock
import sys
from io import StringIO
import pep8
import inspect
import console
import os
from models import *
HBNBCommand = console.HBNBCommand


class TestHBNBCommandDoc(unittest.TestCase):
    '''
    calss to check documentation for HBNBCommand class
    '''

    @classmethod
    def setUpClass(cls):
        ''' This method run before all test and
            find into HBNBCommand class all functions.
            it store in a list of tuples
        '''
        cls.list_base_functions = inspect.getmembers(
            HBNBCommand, inspect.isfunction)

    def test_pep8_console_class(self):
        ''' Test that console.py conforms to PEP8 '''
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in console.py")

    def test_pep8_console_test(self):
        ''' Test that tests/test_console.py conforms to PEP8 '''
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_console.py")

    def test_module_documentation(self):
        ''' check module documentation '''
        doc = True
        try:
            len(console.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} module"
        self.assertEqual(
            True, doc, mesg.format(console.__name__))

    def test_class_documentation(self):
        ''' check class HBNBCommand documentation '''
        doc = True
        try:
            len(HBNBCommand.__doc__) >= 1
        except Exception:
            doc = False
        mesg = "No documentation found for {} class"
        self.assertEqual(
            True, doc, mesg.format(HBNBCommand.__name__))

    def test_functions(self):
        ''' check documentation for every function '''
        for item in self.list_base_functions:
            function = item[1]
            if str(function).find("function Cmd") != -1:
                continue
            doc = True
            try:
                len(function.__doc__) >= 1
            except Exception:
                doc = False
            mesg = "No documentation found for < def {} > function"
            self.assertEqual(
                True, doc, mesg.format(function.__name__))


class TestHBNBCommand(unittest.TestCase):
    ''' Test for HBNBCommand class '''
    @classmethod
    def setUpClass(cls):
        cls.path_file = 'file.json'

    def setUp(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists(self.path_file):
            os.remove(self.path_file)

    def with_mock(self, cmd, expected):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            HBNBCommand().onecmd(cmd)
            output = std_out.getvalue()
            self.assertEqual(output.strip(), expected.strip())

    def test_console_help(self):
        expected = ("Documented commands (type help <topic>):\n"
                    "========================================\n"
                    "EOF  all  create  destroy  help  quit  show  update\n")
        self.with_mock(cmd="help", expected=expected)

    def test_exit(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create(self):
        self.with_mock(cmd="create", expected="** class name missing **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="create MyModel",
                       expected="** class doesn't exist **")

    def test_show(self):
        self.with_mock(cmd="show", expected="** class name missing **")
        self.with_mock(cmd="show MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="show BaseModel",
                       expected="** instance id missing **")

    def test_destroy(self):
        self.with_mock(cmd="destroy", expected="** class name missing **")
        self.with_mock(cmd="destroy MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="destroy BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="destroy BaseModel 121212",
                       expected="** no instance found **")

    def test_all(self):
        self.with_mock(cmd="all MyModel",
                       expected="** class doesn't exist **")

    def test_update(self):
        self.with_mock(cmd="update", expected="** class name missing **")
        self.with_mock(cmd="update MyModel",
                       expected="** class doesn't exist **")
        self.with_mock(cmd="update BaseModel",
                       expected="** instance id missing **")
        self.with_mock(cmd="update BaseModel 121212",
                       expected="** no instance found **")

    def test_create_object(self):
        output = ""
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Amenity")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create BaseModel")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create City")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Place")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create Review")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create State")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            FileStorage._FileStorage__objects = {}
            storage = FileStorage()
            HBNBCommand().onecmd("create User")
            output = std_out.getvalue()
            list_obj = list(storage.all().values())
            self.assertEqual(output.strip(), list_obj[0].id)

    def test_show_object(self):

        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = base_model.BaseModel()
            HBNBCommand().onecmd("show BaseModel {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = city.City()
            HBNBCommand().onecmd("show City {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = place.Place()
            HBNBCommand().onecmd("show Place {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = review.Review()
            HBNBCommand().onecmd("show Review {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = state.State()
            HBNBCommand().onecmd("show State {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            base = user.User()
            HBNBCommand().onecmd("show User {}".format(base.id))
            output = std_out.getvalue()
            self.assertEqual(output.strip(), str(base))
