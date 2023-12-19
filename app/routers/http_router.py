# Standard Library
import json
from typing import Any
from urllib.parse import parse_qs

# Third Party Library
from actions.hello_action import HelloAction
from asgiref.typing import ASGIReceiveCallable, HTTPScope


async def receive_body(receive: Any) -> str:
    body = b""
    more_body = True
    while more_body:
        message = await receive()
        body += message.get("body", b"")
        more_body = message.get("more_body", False)
    return body.decode()


def parse_query_string(query_string: bytes) -> dict:
    # バイト文字列をデコードして、URLエンコードされたクエリパラメーターを解析
    parsed = parse_qs(query_string.decode())
    # リスト値から単一の値に変換（単一の値のみを期待する場合）
    return {k: v[0] for k, v in parsed.items()}


# ルーターではリクエストを受け取ってアクションを実行しレスポンスを返却する。リクエストやレスポンスの内容はアクションに委譲する
async def http_router(scope: HTTPScope, receive: ASGIReceiveCallable) -> tuple[bytes, bytes]:
    path = scope["path"]
    if path == "/":
        hello_action = HelloAction()
        # リクエストボディを受け取る
        body = await receive_body(receive)
        return hello_action.run(body)
    elif path == "/user" and scope["method"] == "POST":
        # リクエストボディを受け取る
        event = receive()
        return b"application/json", json.dumps({"message": {"message": f"とりあえずPOSTはできたからいい加減な値を返す"}}).encode()
    else:
        # 本当に適当なレスポンスを作成したい時はこのように直接書くこともできる
        return b"application/json", json.dumps({"message": "Not Found"}).encode()
