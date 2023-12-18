# Third Party Library
from stores.store import Store


class HelloDto:
    def __init__(self, greeting: str):
        self.greeting = greeting


class HelloStore(Store):
    def __init__(self):
        pass

    def insert_greeting(self, greeting: str):
        query = f"INSERT INTO greetings (greeting) VALUES (%s)"
        self.insert_data(query, greeting)

    def get_by_user_id(self, user_id: str) -> HelloDto:
        query = f"SELECT greeting FROM greetings WHERE user_id = %s"
        return self.fetch_data(query, user_id)
