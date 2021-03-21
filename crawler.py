import crawler
import graphs.igraphCreator

fetcher = crawler.WebsiteFetcher()  # pylint: disable=no-member
fetcher.add_website("https://bytewerk.org")

for website in fetcher.fetch(10):
    for link in website:
        print(link)

graph = graphs.igraphCreator.NetworkGraph(fetcher)
graph.create()
