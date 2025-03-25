from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка подключения к БД
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Создание движка для подключения к БД
engine = create_engine(DATABASE_URL)

# Создание базового класса для всех моделей данных
Base = declarative_base()

# Создание фабрики сессий для взаимодествия с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
