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
    x = re.compile("([a-zA-Z0-9']+[.?!,]?)+")
    t = x.findall(page.content)
    m = {}
    length = random.randint(80, 120)
    for i in range(len(t)):
        w = []
        c = t[i]
        for y in range(len(t) - 1):
            if c == t[y]:
                w.append(str(t[y + 1]))
        m[c] = w
    content = []
    x = random.choice(list(m.keys()))
    for i in range(length):
        if len(m[x]) == 0:
            break
        y = random.choice(m[x])
        content.append(y)
        x = y
    return page.url, ' '.join(content)
