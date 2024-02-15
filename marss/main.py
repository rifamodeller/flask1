from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()
    for i in range(4):
        user_data = {
            'surname': f'Scott{i}',
            'name': 'Ridley',
            'age': '21',
            'position': 'captain',
            'speciality': 'research engineer',
            'address': 'module_1',
            'email': f'scott_chief{i}@mars.org'
        }
        user = User(**user_data)
        session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
