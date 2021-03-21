import crawler
import graphs.igraphCreator
import os


fetcher = crawler.WebsiteFetcher(wait_time_max = 2)  # pylint: disable=no-member
# fetcher.add_website("https://bytewerk.org")
# fetcher.add_website("https://blog.bytewerk.org")
# fetcher.add_website("https://gaestehausleeste.de")
fetcher.add_website("https://k-tronik.de")

for website in fetcher.fetch(10):
    for link in website:
        print(link)

graph = graphs.igraphCreator.NetworkGraph(fetcher)
graph.create()

os.startfile("plot.html")
