import bs4 as bs
import urllib.request

def path_to_philosophy(topic):
    main = 'http://en.wikipedia.org/wiki/'

    visited_pages = list()

    def find_path(topic):
        def valid_link(node):
            # not an external link
            # not a link to current page
            # not a link to non-existent page
            return node.name == 'a' and node['href'].startswith('/wiki/') and \
                   (topic + '#') not in node['href'] and \
                   'page does not exist' not in node['title']

        print(topic)

        if topic == "Philosophy":
            print("We reached Philosophy!")
            return True

        if topic in visited_pages:
            print("We went into a loop!")
            return False

        visited_pages.append(topic)

        try:
            request = urllib.request.urlopen(main + topic)
            html = bs.BeautifulSoup(request.read(), 'lxml')

            paragraphs = html.select("#mw-content-text > .mw-parser-output > p")

            for paragraph in paragraphs:
                parantheses_count = 0
                for node in paragraph.contents:
                    try:
                        parantheses_count += node.string.count('(') - node.string.count(')')
                    except Exception:
                        continue
                    if parantheses_count == 0 and valid_link(node):
                        return find_path(node['href'].replace('/wiki/', ''))
        except Exception:
            print("No such page exist!")
            return False

    return find_path(topic)

path_to_philosophy('Greek_language')