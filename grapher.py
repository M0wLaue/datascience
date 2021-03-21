import graphs.igraphCreator
import os
import pickle

website_data = None
with open("fetcher.data", "rb") as input_file:
    website_data = pickle.load(input_file)

graph = graphs.igraphCreator.NetworkGraph(website_data)
graph.create()

os.startfile("plot.html")