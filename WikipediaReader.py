import requests
import re
import graphviz

def extractLinks(link):
    response = requests.get(link)
    if response is not None:
        pattern = r'<a\s+href=[\'"]?([^\'" >]+)[\'"]?'
        links = re.findall(pattern, response.text)
        return links

def knowledgeTree(links, origin):

    dot = graphviz.Digraph()
    filtered_links = [link.split("/")[2] for link in links if("/wiki/" in link and link.count("/")==2)]
    count = 1
    dot.node("node0", origin.split("/wiki/")[1])
    for link in filtered_links:
        new_label = "node"+str(count)
        dot.node(new_label, link)
        dot.edge("node0", new_label)
        count=count+1

    dot.attr(layout='circo')
    dot.render('graph',format='pdf')

    return

def main():
    origin = "https://en.wikipedia.org/wiki/Main_Page";
    links = extractLinks(origin)
    knowledgeTree(links, origin)

main()