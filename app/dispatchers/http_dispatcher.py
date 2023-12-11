# Standard Library
from typing import Any

# Third Party Library
from asgiref.typing import ASGIReceiveCallable, ASGISendCallable, HTTPScope
from routers.http_router import http_router
from template import render_template


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
        # ここではエラー起因の白い画面を出さないようにするためにエラーページをレンダリングする
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
