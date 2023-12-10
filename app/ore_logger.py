# Standard Library
import logging
import os


class NewRelicHandler(logging.Handler):
    def emit(self, record) -> None:
        # ここにNew Relicへのログ送信のコードを実装します。
        # 例えば、New RelicのAPIを呼び出すなど。
        pass


def setup_logger():
    logger = logging.getLogger("ore_logger")
    logger.setLevel(logging.DEBUG)

    # 標準出力へのハンドラーを設定
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stdout_handler.setFormatter(formatter)
    # # 本番環境の場合、New Relicハンドラーを設定
    # if os.getenv("ENVIRONMENT") == "production":
    #     newrelic_handler = NewRelicHandler()
    #     newrelic_handler.setLevel(logging.ERROR)  # ここで必要なログレベルを設定
    #     # ここでカスタム設定を入れることも可能
    #     logger.addHandler(newrelic_handler)

    logger.addHandler(stdout_handler)

    return logger


# ロガーをセットアップ
logger = setup_logger()

# ログの使用例
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
