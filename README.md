# ENViscerate

One line access to environment variables, handling typecasts automatically. Simply declare a variable with the same name, assigning it to the output of the function ``env(default_value)`` where ``default_value`` is of the type you want the env variable casted as. It is easier to say with an example

```python
from enviscerate import env
HOME = env('/this/dir')
```

Will set the value of HOME to the first available value with the following priority:

1. env var ``$HOME``
2. .env file supplied value
3. value ``'/this/dir'`` you supplied to env() function above


features
--------

- if type is dict, it will be parsed as JSLOB using jsonofabitch module(if available). parsed as JSON using builtin json.loads() otherwise
- if bool it will be set to ``True`` if ``str(val).lower() in ["t", "true", "1", "yes", "y"]`` for ``env(val)`` and ``False`` otherwise
- If ``None``, the case of ``env()``, you will get ``None`` if the variable is not declared and a string otherwise
- otherwise it will be casted as whatever you supply. presumably an ``int`` ``float`` or ``str`` but with no presumptions or restrictions thereof
- It will use dotenv if available but does not require it, but will spit warnings to avoid frustrating mysterious why-are-my-settings-not-registering hickups


how does it work
----------------

it is a hack that stack traces the function call to pull the variable name it was assigned to which is then used to pull the env variable sharing the same name. env vars are implicitly delivered as strings so they have to be typecasted, the information for that is pulled out of the default value you give as the argument to env. I made this because i was sick of looking at the code i was using to do this typecasting. 
