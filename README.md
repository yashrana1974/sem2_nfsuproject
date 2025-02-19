# sem2_nfsuproject
College Project Central Storage

Networking Tool

# *Create a requirements.txt*
Pip Freeze is a command used in Python to freeze the current state of a virtual environment. This command creates a list of all the installed packages in the virtual environment, along with their versions. This list can be used later to recreate the same virtual environment on another machine.

requirements.txt file instead of including the virtualenv itself.

You can easily generate this file with the following: pip freeze > requirements.txt You can then install the virtualenv packages on the target machine with: pip install -r requirements.txt

It is important to note that including the virtualenv will often not work at all as it may contain full paths for your local system. It is much better to use a requirements.txt file.
