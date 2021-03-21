import graphs.igraphCreator
import os
import pickle
import zlib

website_data = None

sites = set()
sites.add("https://bytewerk.org")
sites.add("https://blog.bytewerk.org")
sites.add("https://stats.bytewerk.org")
sites.add("https://gaestehausleeste.de")
sites.add("https://k-tronik.de")
sites.add("https://k-tronik.digital")
sites.add("https://mantis.zettacloud.de")
sites.add("https://toyako.de")
sites.add("https://wttr.in")

while len(sites) != 0:
    site = sites.pop()
    filename = zlib.crc32(bytearray(site, encoding="utf-8"))
    with open(os.path.join("data", str(filename)), "rb") as input_file:
        website_data = pickle.load(input_file)

    graph = graphs.igraphCreator.NetworkGraph(website_data)
    graph.create()

    os.startfile("plot.html")