# sem2_nfsuproject
College Project Central Storage

Networking Tool

*Create a requirements.txt*
As was mentioned in a comment it is standard to do this through a requirements.txt file instead of including the virtualenv itself.

You can easily generate this file with the following: pip freeze > requirements.txt You can then install the virtualenv packages on the target machine with: pip install -r requirements.txt

It is important to note that including the virtualenv will often not work at all as it may contain full paths for your local system. It is much better to use a requirements.txt file.
