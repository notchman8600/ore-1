# Third Party Library
import pymysql
from dbutils.pooled_db import PooledDB


class DatabasePool:
    def __init__(self) -> None:
        # PooledDBを使用してコネクションプールを作成
        self.pool = PooledDB(
            creator=pymysql,  # 使用するDBAPI
            maxconnections=6,  # プールする最大接続数
            host="ホスト名",
            user="ユーザー名",
            passwd="パスワード",
            db="データベース名",
        )

    def get_connection(self):
        return self.pool.connection()


class Store(DatabasePool):
    def __init__(self):
        super().__init__()

    def fetch_data(self, query):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def insert_data(self, query, data):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
