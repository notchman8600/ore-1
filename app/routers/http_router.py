# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, HTTPScope

# First Party Library
from app.actions.hello_action import HelloAction


# ルーターではリクエストを受け取ってアクションを実行しレスポンスを返却する。リクエストやレスポンスの内容はアクションに委譲する
def http_router(scope: HTTPScope, receive: ASGIReceiveCallable) -> tuple[bytes, bytes]:
    path = scope["path"]
    if path == "/":
        hello_action = HelloAction()
        return hello_action.run()
    elif path == "/user" and scope["method"] == "POST":
        # リクエストボディを受け取る
        event = receive()
        return b"application/json", json.dumps({"message": {"message": f"とりあえずPOSTはできたからいい加減な値を返す"}}).encode()
    else:
        # 本当に適当なレスポンスを作成したい時はこのように直接書くこともできる
        return b"application/json", json.dumps({"message": "Not Found"}).encode()
