import os

from jinja2 import Environment, FileSystemLoader


def create_html(**kwargs):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('main.html')
    output_from_parsed_template = template.render(kwargs)

    if not os.path.exists('outputs'):
        os.mkdir('outputs')

    with open(f"outputs/{kwargs['target_user']}.html", "w", encoding="utf-8") as f:
        f.write(output_from_parsed_template)

