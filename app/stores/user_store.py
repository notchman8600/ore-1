# Third Party Library
from stores.store import Store


class FetchUserDto:
    def __init__(self, user_id: str, user_name: str):
        self.user_id = user_id
        self.user_name = user_name


class UserStore(Store):
    def __init__(self):
        pass

    def fetch_user(self, user_id: str) -> FetchUserDto:
        query = f"SELECT * FROM users WHERE user_id = %s"
        return self.fetch_data(query, user_id)

    def insert_user(self, user_id: str, user_name: str):
        query = f"INSERT INTO users (user_id, user_name) VALUES (%s, %s)"
        self.insert_data(query, (user_id, user_name))
