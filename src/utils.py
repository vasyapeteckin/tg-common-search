from jinja2 import Environment, FileSystemLoader


def create_html(**kwargs):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('main.html')
    output_from_parsed_template = template.render(kwargs)

    with open(f"outputs/{kwargs['target_user']}.html", "w", encoding="utf-8") as f:
        f.write(output_from_parsed_template)


if __name__ == '__main__':
    # create_html(target_name="vaas=ya", chats=[{'title': '1'}, {'title': '2'}, {'title': '3'}, {'title': '4'}])
    ...
