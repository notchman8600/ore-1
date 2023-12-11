# Third Party Library
from actions.action import Action

# First Party Library
from app.template import render_template


class HelloAction(Action):
    def __init__(self) -> None:
        super().__init__("hello", "say hello", {"name": "string"})

    def run(self) -> tuple[bytes, bytes]:
        # Actionでレスポンスを作成する
        content = render_template("index.jinja2.html", {"message": "hello, I am variable value."})
        return b"text/html", content.encode()
