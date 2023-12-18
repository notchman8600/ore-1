# Third Party Library
from repositories.hello_repository import HelloRepository


class UserGreetingDto:
    def __init__(self, user_id: str, user_name: str, greeting: str):
        self.user_id = user_id
        self.user_name = user_name
        self.greeting = greeting


class HelloController:
    def __init__(self) -> None:
        self.hello_repository = HelloRepository()
        pass

    def get_hello(self, user_id: str) -> UserGreetingDto:
        user_greeting = self.hello_repository.get_hello(user_id)
        return UserGreetingDto(user_greeting.user_id, user_greeting.name, user_greeting.greeting)
