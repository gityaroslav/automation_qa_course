from data.data import Person, Color
from faker import Faker
import random

fake = Faker()
Faker.seed()


def generated_person():
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
        mobile=fake.msisdn(),
        date_of_birth=fake.date_between(start_date='-70y', end_date='today').strftime('%d %b %Y'),

    )


def generated_file():
    path = rf'C:\Users\Slava\PycharmProjects\automation_qa_course\filetest{random.randint(1, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(1, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )
