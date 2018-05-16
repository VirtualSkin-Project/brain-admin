# API constants

# API response
JSON = 'application/json'
TYPE_ERROR = 'Type of parameter \'{}\' is invalid'

# HTTP Verbs
V_POST = 'POST'
V_GET = 'GET'
V_PUT = 'PUT'
V_PATCH = 'PATCH'
V_DELETE = 'DELETE'

ALL = [
    V_POST, V_GET, V_PUT, V_PATCH, V_DELETE
]
VIEW = [
    V_GET
]
EDIT = [
    V_POST, V_PUT, V_PATCH
]
DELETE = [
    V_DELETE
]

# HTTP Status code
OK = 200
CREATED = 201
NOT_FOUND = 404
METHOD_NOT_ALLOWED = 405
CONFLICT = 409
I_M_A_TEAPOT = 418

