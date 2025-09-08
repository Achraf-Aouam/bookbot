


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def get_number_words(filepath):
    return len(get_book_text(filepath).split())

def count_characters(filepath):
    text =  get_book_text(filepath).lower()
    mem = {}
    for i in text:
        mem[i] = mem.get(i , 0)+1

    memitems = list(mem.items())
    memitems.sort(reverse=True, key=lambda x:x[1])
    return memitems