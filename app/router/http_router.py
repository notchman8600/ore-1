# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPRequestEvent, HTTPScope
from template import render_template


def http_router(scope: HTTPScope, receive: ASGIReceiveCallable) -> tuple[bytes, bytes]:
    path = scope["path"]
    if path == "/":
        content = render_template("index.jinja2.html", {"message": "hello, I am variable value."})
        return b"text/html", content.encode()
    elif path == "/user" and scope["method"] == "POST":
        # リクエストボディを受け取る
        event = receive()
        return b"application/json", json.dumps({"message": {"message": f"とりあえずPOSTはできたからいい加減な値を返す"}}).encode()
        # request_body = validate_create_user_request(event)
        # return {"message": f"hello, {request_body['name']}"}
        # assert event["type"] == "http.request"
        # request_body = json.loads(event["body"].decode())
        # return {"message": f"hello, {request_body['name']}"}

    else:
        return b"application/json", json.dumps({"message": "Not Found"}).encode()


async def dispatch_http_event(scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None:
    content_type, encoded_res = http_router(scope, receive)
    # レスポンスヘッダ
    headers = [
        (b"content-type", content_type),
        (b"content-length", str(len(encoded_res)).encode(encoding="utf-8")),
    ]
    await send({"type": "http.response.start", "status": 200, "headers": headers})
    await send({"type": "http.response.body", "body": encoded_res})

    return
