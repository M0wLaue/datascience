class CrawledWebsite():
    def __init__(self, link, depth):
        self.link = link
        self.crawled = False
        self.linklist = []
        self.depth = depth
    def set_link_list(self, link_list):
        self.linklist = link_list
        self.crawled = True
    def iscrawled(self):
        return self.crawled