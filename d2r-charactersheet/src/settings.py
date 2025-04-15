from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "postgresql+psycopg2://postgres:postgres@db:5432/d2r-charactersheet"
    # TEST_DATABASE_URI: str = 'sqlite:////tests/test.db'


settings = Settings()