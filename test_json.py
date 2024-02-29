import json
from models.users import User
user_data = {
    '23532423': {
        'username': 'Unti1',
        'first_name': 'Артём',
        'mail': 'kostyuchenko.work@gmail.com',
        'game_name': 'fggg',
        'market_name': 'unti1'
    },
    '252523255': {
        'username': 'User2342',
        'first_name': 'Егор',
        'mail': 'egor.2524@gmail.com',
        'game_name': 'vvv',
        'market_name': 'eGoR244'
    }
}

# Как идет заполнение пользователя в словарь
u = User(id = 1, username= 'User344', first_name= 'Антон')
u.mail = 'mymail@mail.ru'
u.game_name = 'deeproat galactic'
u.market_name = 'UUUSer433'
user_data.update(u.to_dict())


with open('test.json', 'w', encoding='utf-8') as fl:
    json.dump(user_data, fl, indent=4, ensure_ascii=False)




