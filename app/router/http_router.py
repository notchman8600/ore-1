# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPScope


def http_router(scope, receive) -> dict[str, Any]:
    path = scope["path"]
    if path == "/":
        return {"message": "hello"}

    else:
        return {"message": "Not Found"}


async def dispatch_http_event(scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable):
    res: dict[str, Any] = http_router(scope, receive)
    res = json.dumps(res).encode()
    # レスポンスヘッダ
    headers = [
        (b"content-type", b"application/json"),
        (b"content-length", str(len(res)).encode()),
    ]
    await send({"type": "http.response.start", "status": 200, "headers": headers})
    await send({"type": "http.response.body", "body": res})

    return
