from duckduckgo_search import DDGS


def search_web(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))

    if not results:
        return "No results found."

    output = ""

    for r in results:
        output += f"{r['title']}\n{r['body']}\n{r['href']}\n\n"

    return output