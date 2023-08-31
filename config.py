domain.config["DATABASES"]["default"] = {
    "PROVIDER": "protean.adapters.repository.sqlalchemy.SAProvider",
    "DATABASE": "SQLITE",
    "DATABASE_URI": "sqlite:///quickstart.db",
}