import igraph
import graphs.plotlyCreator  # pylint: disable=import-error

vertex_size_max = 50

class NetworkGraph():
    def __init__(self, fetcher):
        self.fetcher = fetcher
        self.graph = igraph.Graph(directed=True)
        self.urls = []
        self.types = []
        self.depths = []
    
    def create(self):
        for website in self.fetcher.website_list.values():
            if website.link not in self.urls:
                self.graph.add_vertex()
                self.urls.append(website.link)
                self.types.append('internal')
                self.depths.append(website.depth)
            website_index = self.urls.index(website.link)
            for external_link in website.external_linklist:
                if external_link not in self.urls:
                    self.graph.add_vertex()
                    self.urls.append(external_link)
                    self.types.append('external')
                    self.depths.append(10)
                external_link_index = self.urls.index(external_link)
                self.graph.add_edge(website_index, external_link_index)
            for internal_link in website.linklist:
                if internal_link not in self.urls:
                    self.graph.add_vertex()
                    self.urls.append(internal_link)
                    self.types.append('internal')
                    self.depths.append(self.fetcher.website_list[internal_link].depth)
                internal_link_index = self.urls.index(internal_link)
                self.graph.add_edge(website_index, internal_link_index)

        # Vertex attributes
        self.graph.vs['urls'] = self.urls
        self.graph.vs['types'] = self.types
        # self.graph.vs["label"] = self.graph.vs["urls"]
        color_dict = {"internal": "blue", "external": "red"}
        self.graph.vs["color"] = [color_dict[_type] for _type in self.graph.vs["types"]]
        self.graph.vs["size"] = list(map(lambda depth: vertex_size_max / (depth+1), self.depths))

        # Selecting Layout
        # Kamada-Kawai
        # for more information see:
        # https://www.cs.rhul.ac.uk/home/tamas/development/igraph/tutorial/tutorial.html
        layout = self.graph.layout("kk")
        # igraph.plot(self.graph, layout=layout)

        graphs.plotlyCreator.create_plotly_plot(
            layout,
            len(self.urls),
            [e.tuple for e in self.graph.es],
            self.urls,
            [color_dict[_type] for _type in self.graph.vs["types"]],
            list(map(lambda depth: vertex_size_max / (depth + 1), self.depths))
        )
