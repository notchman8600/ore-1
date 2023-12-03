# Standard Library
import json

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPRequestEvent, HTTPScope, Scope
from router.http_router import dispatch_http_event


async def app(scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None:
    # JSONデータを準備
    response_data = json.dumps({"message": "Hello, world"}).encode()

    try:
        if scope["type"] == "http":
            # scope["type"] == "http" であることを期待してhttpリクエストに紐付くイベントを処理
            assert type(scope) == HTTPScope
            await dispatch_http_event(scope, receive, send)
    except Exception as e:
        # ここでの例外はイベント起動に関わる例外のみで、アプリケーションレベルの例外はdispatcherのハンドラで全て処理を行う
        pass

    # # レスポンスの開始を送信
    # await send({"type": "http.response.start", "status": 200, "headers": headers})

    # # レスポンス本文を送信
    # await send(
    #     {
    #         "type": "http.response.body",
    #         "body": response_data,
    #     }
    # )
    return
