import re
import random
import wikipedia


def get_wikipedia_content(search_query):
    search_results = wikipedia.search(query=search_query, results=1)  # Get the top result

    if not search_results or not len(search_results):
        return ''
    return wikipedia.page(search_results[0])


def generate(search_query):
    page = get_wikipedia_content(search_query)
    if not page or not page.content or len(page.content) == 0:
        return False
    regex = re.compile("([a-zA-Z0-9']+[.?!,]?)+")
    results = regex.findall(page.content)
    num_results = len(results)
    next_words = {}
    length = random.randint(80, 120)
    for i in range(num_results):
        w = []        
        for y in range(num_results - 1):
            if results[y].lower() == results[i].lower():
                w.append(str(results[y + 1]))
        next_words[results[i]] = w
    content = []
    x = random.choice(list(next_words.keys()))
    for i in range(length):
        if len(next_words[x]) == 0:
            break
        y = random.choice(next_words[x])
        content.append(y)
        x = y
    return page.url, ' '.join(content)
