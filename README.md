# The AirBNB clone Console

![hbnb](./hbtn.png)

## About
HBNB Console

This is a command-line interface for the Holberton School's AirBnB clone project, allowing the user to manage their database of objects.

## Background Context 

[![AirBNB-clone](https://img.youtube.com/vi/XRH_8w1DEGI/0.jpg)](https://youtu.be/XRH_8w1DEGI "AirBNB clone")

## Getting Started
To get started with the HBNB Console, clone the repository and install the requirements.

```
$ git clone https://github.com/username/AirBnB_clone.git
$ cd AirBnB_clone
$ pip install -r requirements.txt
```
Usage

To start the HBNB Console, run console.py with Python3.

bash
```
$ ./console.py
```
The console prompt will appear as follows:


```
File not found
Welcome to the HBNB console!
(hbnb) 
```
The following commands are available to manage the database of objects:

## quit
Exit the program.

bash
```
(hbnb) quit
$
```
## EOF

Exit the console using EOF (Ctrl-D).


```
(hbnb) Ctrl-D
$
```
## create

Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id.


```
(hbnb) create BaseModel
bba240d3-3a3a-41c8-9c12-cfdb2641cf06
```
## show

Prints the string representation of an instance based on the class name and id.


```
(hbnb) show BaseModel bba240d3-3a3a-41c8-9c12-cfdb2641cf06
[BaseModel] (bba240d3-3a3a-41c8-9c12-cfdb2641cf06) {'id': 'bba240d3-3a3a-41c8-9c12-cfdb2641cf06', 'created_at': datetime.datetime(2023, 2, 11, 15, 6, 22, 758157), 'updated_at': datetime.datetime(2023, 2, 11, 15, 6, 22, 758199)}
```
## destroy

Deletes an instance based on the class name and id.


```
(hbnb) destroy BaseModel bba240d3-3a3a-41c8-9c12-cfdb2641cf06
```
## all

Prints all string representation of all instances based or not on the class name.

bash
```
(hbnb) all BaseModel
[BaseModel] (3f3b3c3a-c1b8-4c5d-9d39-23212e99cbf8) {'id': '3f3b3c3a-c1b8-4c5d-9d39-23212e99cbf8', 'created_at': datetime.datetime(2023, 2, 11, 15, 6, 36, 975983), 'updated_at': datetime.datetime(2023, 2, 11, 15, 6, 36, 975996)}
```
## update

Updates an instance based on the class name and id by adding or updating attribute.

bash
```
(hbnb) update BaseModel 3f3b3c3a-c1b8-4c5d-9d39-23212e99cbf8 first_name "Betty"
```
Built With

    Python3

Authors

	Roy Kiplagat  bagoviggo@gmail.com
	Tony Maiyo    tonymaiyo008@gmail.com

License

<details>
	
### First step: Write a command interpreter to manage the AirBnB objects.

This is the first step towards building the first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called ```BaseModel```) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (```User```, ```State```, ```City```, ```Place```…) that inherit from ```BaseModel```
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources
__Read or watch__:
1. [cmd module](https://docs.python.org/3.8/library/cmd.html)
2. [cmd module in depth](http://pymotw.com/2/cmd/)
3. [uuid module](https://docs.python.org/3.8/library/uuid.html)
4. [datetime](https://docs.python.org/3.8/library/datetime.html)
5. [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
6. [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
7. [python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
8. [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
9. [python unittests](https://realpython.com/python-testing/)


## Learning objectives
By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) without the help of __Google__

* [X] How to create a Python package
* [X] How to create a command interpreter in Python using the cmd module
* [X] What is Unit testing and how to implement it in a large project
* [X] How to serialize and deserialize a Class
* [X] How to write and read a JSON file
* [X] How to manage datetime
* [X] What is an UUID
* [X] What is *args and how to use it
* [X] What is **kwargs and how to use it
* [X] How to handle named arguments in a function


## More info
The shell should look like this in interactive mode.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode:``` $ echo "python3 -m unittest discover tests" | bash```

![console](./console.png)

[![AirBNB-clone](https://img.youtube.com/vi/1mAC9x3aixE/0.jpg)](https://youtu.be/1mAC9x3aixE "AirBNB clone")

## Tasks
### Task 3
* Write a class `BaseModel` that defines all common attributes/methods for other classes:
	* `models/base_model.py`
	* Public instance attributes:
		* `id`: string - assign with an `uuid` when an instance is created:
			* you can use `uuid.uuid4()` to generate unique id but don’t forget to convert to a string
			* the goal is to have unique `id` for each `BaseModel`
		* `created_at`:  datetime - assign with the current datetime when an instance is created
		* `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
	* `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
* Public instance methods:
	* `save(self)`:updates the public instance attribute `updated_at` with the current datetime
	* `to_dict(self)`:  returns a dictionary containing all keys/values of `__dict__` of the instance:
		* by using `self.__dict__`, only instance attributes set will be returned
		* a key `__class__` must be added to this dictionary with the class name of the object
		* `created_at` and `updated_at` must be converted to string object in ISO format:
			* format: `%Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)`
			* you can use `isoformat()` of `datetime` object
		* This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our `BaseModel`

### Task 4
* Previously we created a method to generate a dictionary representation of an instance (method `to_dict()`).
* Now it’s time to re-create an instance with this dictionary representation.
```<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>```
* Update `models/base_model.py`:
	* `__init__(self, *args, **kwargs)`:
		* you will use `*args`, `**kwargs` arguments for the constructor of a `BaseModel`. (more information inside the AirBnB clone concept page)
		* `*args` won’t be used
		* if `kwargs` is not empty:
			* each key of this dictionary is an attribute name (Note `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
			* each value of this dictionary is the value of this attribute name
			* **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into `datetime` object. Tip: you know the string format of these datetime
		* Otherwise:
			* create `id` and `created_at` as you did previously (new instance)


### Task 5
 Now we can recreate a `BaseModel` from another one by using a dictionary representation:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won’t be relevant:

-   Python doesn’t know how to convert a string to a dictionary (easily)
-   It’s not human readable
-   Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

Magic right?

Terms:

-   **simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
-   **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

-   `models/engine/file_storage.py`
-   Private class attributes:
    -   `__file_path`: string - path to the JSON file (ex: `file.json`)
    -   `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
-   Public instance methods:
    -   `all(self)`: returns the dictionary `__objects`
    -   `new(self, obj)`: sets in `__objects` the `obj` with key `<obj class name>.id`
    -   `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
    -   `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application

-   import `file_storage.py`
-   create the variable `storage`, an instance of `FileStorage`
-   call `reload()` method on this variable

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`

-   import the variable `storage`
-   in the method `save(self)`:
    -   call `save(self)` method of `storage`
-   `__init__(self, *args, **kwargs)`:
    -   if it’s a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```
</details>
