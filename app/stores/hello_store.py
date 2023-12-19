# Third Party Library
from ore_logger import logger
from stores.store import Store


class HelloDto:
    def __init__(self, greeting: str):
        self.greeting = greeting


class HelloStore(Store):
    def __init__(self):
        super().__init__()
        pass

    def insert_greeting(self, greeting: str):
        query = f"INSERT INTO greetings (comment) VALUES (%s)"
        self.insert_data(query, greeting)

    def get_by_user_id(self, user_id: int) -> HelloDto:
        query = f"SELECT comment FROM greetings WHERE user_id = %s"
        row_data = self.fetch_data(query, user_id)
        assert row_data is not None and len(row_data) == 1, "error, row_data is None or len(row_data) > 1"
        logger.debug(f"row_data: {row_data},{type(row_data[0][0])}")
        return HelloDto(row_data[0][0])
