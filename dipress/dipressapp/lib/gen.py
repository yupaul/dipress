import random
import re
import wikipedia
from collections import defaultdict

def get_wikipedia_content(search_query):
    search_results = wikipedia.search(query=search_query, results=1)

    if not search_results or not len(search_results):
        return ''
    try:
        return wikipedia.page(search_results[0], auto_suggest=False)
    except Exception:
        return ''


def generate(search_query):
    page = get_wikipedia_content(search_query)
    if not page or not page.content or len(page.content) == 0:
        return False

    mchain = defaultdict(list)    
    words = re.split('[\n\r\s]+', page.content)
    length = random.randint(150, 250)

    for i in range(len(words) - 2):
        k = tuple(map(lambda _w: _w.lower(), words[i:i+2]))
        mchain[k].append(words[i+2])
    
    curr = random.choice(list(mchain.keys()))
    output = list(curr)
    
    for i in range(length):
        try:
            _word = random.choice(mchain[curr])
            output.append(_word)
            curr = tuple(map(lambda _w: _w.lower(), [curr[1], _word]))
        except Exception:
            break  

    return page.url, ' '.join(output)
