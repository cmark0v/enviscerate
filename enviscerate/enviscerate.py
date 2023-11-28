"""
Declare with the same name as the environment variable you wish to access

HOME = env('/this/dir')

will set the value of HOME with priority:
    1. env var $HOME
    2. .env file supplied value(if present and module dotenv available)
    3. value you supplied to env() function above

if type is dict, it will be parsed as JSLOB using jsonofabitch module(if available). parsed as JSON using builtin json.loads() otherwise
if bool it will be set to true if str(val).lower() in ["t", "true", "1", "yes", "y", "on"] for env(val)
otherwise any incomming value from the environment will be cast from its native state as a string to the type of the value supplied to env()
"""

from warnings import warn

try:
    from jsonofabitch import loads
except:
    warn("jsonofabitch module not found, defaulting to builtin json")
    from json import loads
try:
    from dotenv import load_dotenv

    load_dotenv()
except:
    warn("dotenv not found, not loading values from $PWD/.env")


import traceback
from os import getenv

YES = ["t", "true", "1", "yes", "y", "on"]


def env(val):
    (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
    def_name = text[: text.find("=")].strip()
    if type(val) is bool:
        return getenv(def_name, str(val)).lower() in YES
    elif type(val) is dict:
        _envval = getenv(def_name, False)
        if _envval:
            return loads(_envval)
        else:
            return val
    elif val is None:
        return(getenv(def_name,None))
    else:
        return type(val)(getenv(def_name, val))
