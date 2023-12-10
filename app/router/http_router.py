# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPRequestEvent, HTTPScope


def http_router(scope: HTTPScope, receive: ASGIReceiveCallable) -> dict[str, Any]:
    path = scope["path"]
    if path == "/":
        return {"message": "hello"}
    elif path == "/user" and scope["method"] == "POST":
        # リクエストボディを受け取る
        event = receive()
        return {"message": {"message": f"とりあえずPOSTはできたからいい加減な値を返す"}}
        # request_body = validate_create_user_request(event)
        # return {"message": f"hello, {request_body['name']}"}
        # assert event["type"] == "http.request"
        # request_body = json.loads(event["body"].decode())
        # return {"message": f"hello, {request_body['name']}"}

    else:
        return {"message": "Not Found"}


async def dispatch_http_event(scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None:
    res_body: dict[str, Any] = http_router(scope, receive)
    encoded_res = json.dumps(res_body).encode()
    # レスポンスヘッダ
    headers = [
        (b"content-type", b"application/json"),
        (b"content-length", str(len(encoded_res)).encode()),
    ]
    await send({"type": "http.response.start", "status": 200, "headers": headers})
    await send({"type": "http.response.body", "body": encoded_res})

    return
