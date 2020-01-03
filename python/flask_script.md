The Flask-Script extension provides support for writing external scripts in Flask. This includes running a development server, a customised Python shell, scripts to set up your database, cronjobs, and other command-line tasks that belong outside the web application itself.

Flask-Script works in a simlar way to Flask itself. You define and add commands that can be called from the command line to a Manager instance.



## Creating and running commands

The first step is to create a Python module to run your script commanfs in. You can call it anything you like, for our examples we'll call it manage.py.

You don't have to place all your commands in the same file; for example, in a larger project with lots of commands you might want to split them into a number of files with related commands.

In your manage.py file you have to create a Manager instance. The Manager class keeps trace of all the commands and handles how they are called from the command line:

```
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)

if __name__ == '__main__':
	manager.run()
```

