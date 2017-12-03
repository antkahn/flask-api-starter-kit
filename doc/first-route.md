# Creating your first route

You will notice a `routes` folder in the project.
In this folder, there is only a `__init__.py` file for the moment.
This file is present in most python folders. It announces to python that this folder is a python module.
It is used to share and structure code in your app.

The `routes` folder is where you will register your routes. But you shall not write any logic in this folder.
All the logic will be set in the `resources` folder.

In the `routes` folder, create a `user.py` file containing:

```python
"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import UserResource


USER_BLUEPRINT = Blueprint('user', __name__)
Api(USER_BLUEPRINT).add_resource(UserResource, '/user')
```

And add the following line in the `routes/__init__.py` file:
```python
from .user import USER_BLUEPRINT
```

In the `resources` folder, create a `user.py` file containing:

```python
"""
Define the REST verbs relative to the users
"""
from flask.ext.restful import Resource


class UserResource(Resource):
    """ Verbs relative to the users """

    def get(self):
        """ Return a list of key information about users """

        return 'such user'
```

And add the following line in the `resources/__init__.py` file:
```python
from .user import UserResource
```

Then you can go to this url: [http://127.0.0.1:3000/application/user](http://127.0.0.1:3000/application/user).
We have a route!

So what did we do here?

First, we added a BLUEPRINT to our server. We defined a `USER_BLUEPRINT` (if you want more docs about blueprints and flask restful, go [here](http://flask-restful-cn.readthedocs.io/en/0.3.4/api.html)), and it has been registered automatically on the server.
How? By [this line](https://github.com/antkahn/flask-api-starter-kit/blob/master/src/server.py#L39)!
It calls the `register_blueprint` method for each blueprint set in the `__init__.py` file of the `route` folder.

We told our blueprint to use the `UserResource` when querried on the `/user` url.

In this resource, flask restful lets you to create classes containing methods, which names correspond to REST verbs.
For example, we called our resource's method `get`, and when we call an HTTP GET on the `/user` route, this method will be called.
This exists because our `UserResource` class inherit from the flask restful `Resource` class. This class handles all the complexity.

And that's it ! So, when you want to create a new route:
 * Create a new resource
 * Create a new blueprint
 * Register it in the server by exporting it in the `__init__.py` of the route folder


As you can see, each python files starts with documentation on the file. This is called a `docstring`.
If you want to know more on the python standard for doctstrings, read [this](https://www.python.org/dev/peps/pep-0257/).
You should start all your python files with a docstring explaining what they contain, and all your methods and classes should have a docstring, explaining what they do.

--------
### Import and `__init__.py`

Why do we need all those lines in those weird files?
> And add the following line in the `routes/__init__.py` file:
> ```python
> from .user import USER_BLUEPRINT
> ```

The `__init__.py` files tells python that he should consider this folder like a python module.

And what does the line do?
It makes it possible to access the `USER_BLUEPRINT` variable in the `routes` namespace.

Wait what?
If you don't write that line, you would have to write everywhere else
```python
from routes.user import USER_BLUEPRINT
```
Now, you can simply do
```python
from routes import USER_BLUEPRINT
```

which will save you a lot of time in the long run!

------

[Next step !](database.md)
