# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPRequestEvent, HTTPScope


def http_router(scope: HTTPScope, receive: ASGIReceiveCallable) -> dict[str, Any]:
    path = scope["path"]
    if path == "/":
        return {"message": "hello"}
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
