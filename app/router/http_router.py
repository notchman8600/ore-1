# Standard Library
import json
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPRequestEvent, HTTPResponseStartEvent, HTTPScope
from template import render_template

# First Party Library
from app.actions.hello_action import HelloAction


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


async def dispatch_http_event(scope: HTTPScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None:
    # dispatch errorを全体的に囲むことで白い画面を出さないようにする
    # 本当はAPIコールかHTMLコールかによって例外処理を考える必要がある
    # APIコールであればエラーオブジェクトのJSON、HTMLであればエラーページをレンダリングする必要がある
    try:
        content_type, encoded_res = http_router(scope, receive)
        # レスポンスヘッダ
        headers = [
            (b"content-type", content_type),
            (b"content-length", str(len(encoded_res)).encode(encoding="utf-8")),
        ]
        await send({"type": "http.response.start", "status": 200, "headers": headers})
        await send({"type": "http.response.body", "body": encoded_res})
    except Exception as e:
        # HTTPレスポンスの準備
        html_content = render_template("error.jinja2.html", {"message": "hello, I am variable value."})
        await send(
            {
                "type": "http.response.start",
                "status": 500,
                "headers": ((b"content-type", b"text/html"),),
            }
        )
        await send({"body": html_content.encode("utf-8"), "type": "http.response.body"})
    return
