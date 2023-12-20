# Third Party Library
from ore_logger import logger
from stores.store import Store


class FetchUserDto:
    def __init__(self, user_id: int, user_name: str):
        self.user_id = user_id
        self.user_name = user_name


class UserStore(Store):
    def __init__(self):
        super().__init__()
        pass

    def fetch_user(self, user_id: int) -> FetchUserDto:
        query = f"SELECT id, user_name FROM users WHERE id = %s"
        row_data = self.fetch_data(query, user_id)
        # ここは本当はまともに例外を投げるべき
        assert row_data is not None and len(row_data) == 1, "error, row_data is None or len(row_data) > 1"
        logger.debug(f"row_data: {row_data}")
        return FetchUserDto(row_data[0][0], row_data[0][1])

    def insert_user(self, user_id: int, user_name: str):
        query = f"INSERT INTO users (id, user_name) VALUES (%s, %s)"
        self.execute(query, (user_id, user_name))
