# Standard Library
from typing import Any

# Third Party Library
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Jinja2環境のセットアップ
env = Environment(loader=FileSystemLoader("templates/"), autoescape=select_autoescape(["html", "xml"]))


# テンプレートをレンダリングする関数
def render_template(template_name: str, context: Any) -> str:
    template = env.get_template(template_name)
    return template.render(context)
