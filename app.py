from protean import Domain
from protean.fields import String
import json
from protean.globals import current_domain
domain = Domain(__name__)

@domain.aggregate
class User:
    name = String(max_length=50)
    email = String(max_length=50,unique=True)


@domain.application_service
class SignUpService:
    @classmethod
    def signup(cls,name,email):
        user = User(name=name,email=email)
        domain.repository_for(User).add(user)

domain.config["DATABASES"]["default"] = {
    "PROVIDER": "protean.adapters.repository.sqlalchemy.SAProvider",
    "DATABASE": "SQLITE",
    "DATABASE_URI": "sqlite:///quickstart.db",
}

from flask import Flask
from flask import request

app = Flask(__name__)


@app.before_request
def set_context():
    context = domain.domain_context()
    context.push()
@app.route("/users", methods=["GET", "POST"])
def users():
    print("I am coming here")
    if request.method == "POST":
        # user = SignUpService.signup(request.form['name'], request.form['email'])
        return {
            "Hello":"World"
        }
    else:
        users = current_domain.repository_for(User).all()
        return json.dumps([user.to_dict() for user in users]), 200