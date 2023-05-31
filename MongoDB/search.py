from models import Author, Quote

import connect


def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    print(f"Quote with tag '{tag}':")
    for quote in quotes:
        print(f"    ---- {quote.quote}")


def search_by_author(name):
    
    try:
        author = Author.objects(fullname__startswith=value.title())[0]
        quotes = Quote.objects(author=author)
        if quotes:
            result = []
            for quote in quotes:
                r = f"{quote.quote}\n{quote.author.fullname}     tags:{', '.join(quote.tags)}"
                result.append(r)
            return result
    except TypeError as err:
        print(f'err')


def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    print(f"Quotes with tag '{tags}':")
    for quote in quotes:
        print("- {}".format(quote.quote))
    print()


if __name__ == '__main__':
    while True:
        input_command = input("Enter command: ")
        command, value = input_command.split(":")
        command, value = command.strip(), value.strip()
        
        if command == 'name':
            search_by_author(value)
        elif command == 'tag':
            search_by_tag(value)
        elif command == 'tags':
            search_by_tags(value)
        elif command == 'exit':
            break
        else:
            print("Unknown command. Try again")






