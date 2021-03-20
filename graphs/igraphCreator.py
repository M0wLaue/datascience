import igraph
import graphs.plotlyCreator  # pylint: disable=import-error


class NetworkGraph():
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.graph = igraph.Graph()
        self.urls = []
        self.types = []
    
    def create(self):
        for website in self.fetcher.website_list.values():
            if website.link not in self.urls:
                self.graph.add_vertex()
                self.urls.append(website.link)
                self.types.append('internal')
            website_index = self.urls.index(website.link)
            for external_link in website.external_linklist:
                if external_link not in self.urls:
                    self.graph.add_vertex()
                    self.urls.append(external_link)
                    self.types.append('external')
                external_link_index = self.urls.index(external_link)
                self.graph.add_edge(website_index, external_link_index)
            for internal_link in website.linklist:
                if internal_link not in self.urls:
                    self.graph.add_vertex()
                    self.urls.append(internal_link)
                    self.types.append('internal')
                internal_link_index = self.urls.index(internal_link)
                self.graph.add_edge(website_index, internal_link_index)

        self.graph.vs['urls'] = self.urls
        self.graph.vs['types'] = self.types

        # self.graph.vs["label"] = self.graph.vs["urls"]
        color_dict = {"internal": "blue", "external": "red"}
        self.graph.vs["color"] = [color_dict[_type] for _type in self.graph.vs["types"]]

        layout = self.graph.layout("kk")
        igraph.plot(self.graph, layout=layout)

        graphs.plotlyCreator.create_plotly_plot(layout, len(self.urls), [e.tuple for e in self.graph.es], self.urls, [color_dict[_type] for _type in self.graph.vs["types"]])
