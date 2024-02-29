
class User:
    def __init__(self, id, username, first_name) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.mail = ''
        self.game_name = ''
        self.market_name = ''
    
    def to_dict(self):
        return {
            f'{self.id}': {
                'username': self.username,
                'first_name': self.first_name,
                'mail': self.mail,
                'game_name': self.game_name,
                'market_name': self.market_name
           }
        }
    
    def to_str(self):
        return f'[{self.id}] {self.username}({self.first_name}) | {self.mail} | {self.game_name} | {self.market_name}'
    