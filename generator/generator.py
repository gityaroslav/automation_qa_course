from data.data import Person
from faker import Faker
import random

fake = Faker()
Faker.seed()


def genereted_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(10, 80),
        department=fake.name(),
        salary=random.randint(1000, 10000),
        email=fake.email(),
        current_address=fake.address().replace("\n", " "),
        permanent_address=fake.address().replace("\n", " "),

    )
