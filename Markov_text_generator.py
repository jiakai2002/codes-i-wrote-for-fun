from encodings import utf_8
import random
from venv import create

storage = {}


def process_file(file_name):

    with open(file_name, encoding="utf8") as f:
        content = f.read()
        content = content.strip().split()
        return content


def create_storage(content, order=2):

    for i in range(0, len(content) - order):
        prefix = tuple(content[i : i + order])
        suffix = content[i + order]

        if prefix not in storage:
            storage[prefix] = [suffix]

        else:
            storage[prefix].append(suffix)


def write_story(order=2):
    random_prefix = random.choice([key for key in storage])
    story = [x for x in random_prefix]
    current_suffix = random.choice(storage[random_prefix])
    story.append(current_suffix)
    for i in range(200):
        next_prefix = tuple(story[-order:])
        next_suffix = random.choice(storage[next_prefix])
        story.append(next_suffix)
    story = " ".join(story)
    print(story)


create_storage(process_file("hello.txt"))
write_story()
