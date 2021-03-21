from datetime import datetime

class CrawledWebsite():
    def __init__(self, link, depth):
        self.link = link
        self.crawled = False
        self.external_linklist = set()
        self.linklist = set()
        self.depth = depth
        self.maillist = set()
        self.last_update = datetime.now()

    def set_link_list(self, link_list):
        self.linklist = set(filter(lambda x: x.startswith(self.link), link_list))

    def set_external_link_list(self, link_list):
        self.external_linklist = set(filter(lambda x: not x.startswith(self.link), link_list))

    def add_mail(self, mail):
        self.maillist.add(mail)

    def finish_crawling(self):
        self.crawled = True
        self.last_update = datetime.now()

    def iscrawled(self):
        return self.crawled
