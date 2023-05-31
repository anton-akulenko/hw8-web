import json

from models import Author, Quote

def load_authors(file):
    with open(file, 'r', encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            fullname = el.get("fullname")
            born_date = el.get("born_date")
            born_location = el.get("born_location")
            description = el.get("description")

            author = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
            author.save()

def load_quotes(file):
    with open(file, 'r', encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            author = el.get("author")
            quote = el.get("quote")
            tags = el.get("tags")
            
            quotes = Quote(author=author, quote=quote, tags=tags)
            quotes.save()

if __name__ == "__main__":
    load_authors('authors.json')
    load_quotes('quotes.json')