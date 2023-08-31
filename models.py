from protean.fields import String
from .domain import domain
@domain.aggregate
class User:
    name = String(max_length=50)
    email = String(max_length=50,unique=True)