from data.data import Person
from faker import Faker

fake = Faker()
Faker.seed()


def genereted_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        email=fake.email(),
        current_address=fake.address().replace("\n", " "),
        permanent_address=fake.address().replace("\n", " "),
    )
