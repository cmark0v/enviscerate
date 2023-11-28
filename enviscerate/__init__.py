"""
Declare with the same name as the environment variable you wish to access

HOME = env('/this/dir')

will set the value of HOME with priority:
    1. env var $HOME
    2. .env file supplied value(if present and module dotenv available)
    3. value you supplied to env() function above

if type is dict, it will be parsed as JSLOB using jsonofabitch module(if available). parsed as JSON using builtin json.loads() otherwise
if bool it will be set to true if str(val).lower() in ["t", "true", "1", "yes", "y"] for env(val)
otherwise any incomming value from the environment will be cast from its native state as a string to the type of the value supplied to env()
"""


from .enviscerate import env
from .enviscerate import YES

__all__ = [env,YES]

__version__ = "0.0.1"
