from typing import Literal, Dict, Any

POST: str = 'post'
GET: str = 'get'

REQUEST_TYPE = Literal[POST, GET]

DATA = Dict[str, Any]
