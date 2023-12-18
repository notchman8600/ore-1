# Third Party Library
from model.user_greeting import UserGreeting
from stores.hello_store import HelloStore
from stores.user_store import UserStore


class HelloRepository:
    def __init__(self) -> None:
        self.hello_store = HelloStore()
        self.user_store = UserStore()

    def get_hello(self, user_id: str) -> UserGreeting:
        user = self.user_store.fetch_user(user_id)
        greeting = self.hello_store.get_by_user_id(user_id)
        return UserGreeting(user.user_id, user.user_name, greeting.greeting)
