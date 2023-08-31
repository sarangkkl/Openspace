from .domain import domain
from .models import User
@domain.application_service
class SignUpService:
    @classmethod
    def signup(cls,name,email):
        user = User(name=name,email=email)
        domain.repository_for(User).add(user)