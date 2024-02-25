from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Створення з'єднання з базою даних
engine = create_engine("sqlite:///app.db", echo=True)

Session = sessionmaker(bind=engine)

# Визначення базового класу моделі, який використовуватиметься для всіх моделей
class Base(DeclarativeBase):
    ... # буде дикларувати в інший клас

# Функція для створення всіх таблиць в базі даних
def create_db():
    Base.metadata.create_all(engine)

# Функція для видалення всіх таблиць з бази даних
def drop_all():
    Base.metadata.drop_all(engine)

