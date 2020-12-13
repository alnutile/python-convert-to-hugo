import stringcase
import random

"""
Get the data from the db
For each item I want to then write it to the format the the
md system needs
the header area
the more info area maybe or let it do it
the md area
the write each file to a folder
what about images
"""


class Convert:
    heros = [
        "/images/heros/default-hero.jpg",
        "/images/heros/hero-coding.png",
        "/images/heros/hero-messy.png",
        "/images/heros/hero-office.png",
        "/images/heros/hero-space.png",
    ]

    def write_converted_item(self, item, folder="posts"):
        """ write it to the folder id.md """
        item_id = item['id']
        file = open(f"output/{folder}/{item_id}.md", "w")
        file.write(item['output'])
        file.close()

    def random_hero(self):
        """ return one of 5 hero images """
        return random.choice(self.heros)

    def convert_item(self, item):
        """ take the content out of the database and make it work with the new system """
        markdown = None
        header = self.make_header(item)
        body = item['body']
        item['output'] = f"{header}\n{body}"
        return item

    def make_header(self, item):
        """ make the nice header from this """
        header = None
        hero = self.random_hero()
        model_id = f"-{item['id']}"
        title = item['title'].replace("\"", "'").replace("@", "")
        identifier = stringcase.spinalcase(title)
        tags = item['tags']
        date = item['created_at']
        weight = item['created_at'].replace("-", "")
        desc = item['body'][0: 60]

        header = f"""---
title: \"{title}\"
date: {date}
hero: {hero}
menu:
  sidebar:
    name: \"{title}\"
    identifier: {identifier}
    weight: {model_id}
tags: [{tags}]
---
"""

        return header
