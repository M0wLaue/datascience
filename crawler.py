import crawler
import graphs.igraphCreator

fetcher = crawler.WebsiteFetcher()  # pylint: disable=no-member
fetcher.add_website("https://www.bytewerk.org/")

for website in fetcher.fetch(3):
    for link in website:
        print(link)

graph = graphs.igraphCreator.NetworkGraph(fetcher)
graph.create()
