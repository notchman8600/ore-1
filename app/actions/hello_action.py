# Third Party Library
from actions.action import Action
from controllers.hello_controller import controller
from template import render_template


class HelloAction(Action):
    def __init__(self) -> None:
        super().__init__("hello", "say hello", {"name": "string"})

    def run(self, headers: dict, body: dict) -> tuple[bytes, bytes]:
        # Actionでレスポンスを作成する
        res = controller.get_hello(1)
        content = render_template(
            "index.jinja2.html",
            {
                "message": "hello, I am variable value.",
                "name": res.user_name,
                "greeting": res.greeting,
                "user_id": res.user_id,
            },
        )
        return b"text/html", content.encode()
