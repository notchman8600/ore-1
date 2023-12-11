# Standard Library
import json

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, Scope
from ore_logger import logger
from routers.http_router import dispatch_http_event


# ASGIアプリのエントリーポイント
async def app(scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None:
    try:
        if scope["type"] == "http":
            logger.debug("httpリクエストを受け取りました")
            # scope["type"] == "http" であることを期待してhttpリクエストに紐付くイベントを処理
            # 実質的にHTTPリクエストに対するアプリケーションはdispatch_http_eventの中で発火するので全体をハンドリングすることでエラーを逃さないようにする
            # 本番では必要なログ以外uvicornなどの設定で不要なログは全て抑制する
            try:
                await dispatch_http_event(scope, receive, send)
            except Exception as e:
                logger.error(f"error has occured in http event: {e}")
                pass
    except Exception as e:
        # ここでの例外はイベント起動に関わる例外のみで、アプリケーションレベルの例外はdispatcherのハンドラで全て処理を行う
        # ここでトラップされるエラーがあるのか？
        # これはそもそも起動に失敗するケースなので、本来は辿り着くはずがない動作である
        logger.error(f"unexpected error has occured: {e}")
        pass

    return
