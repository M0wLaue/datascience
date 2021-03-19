class CrawledWebsite():
    def __init__(self, link, depth):
        self.link = link
        self.crawled = False
        self.external_linklist = []
        self.linklist = []
        self.depth = depth
        self.maillist = set()

    def set_link_list(self, link_list):
        filtered_linklist = list(filter(lambda x: x.startswith(self.link), link_list))
        self.linklist = filtered_linklist

    def set_external_link_list(self, link_list):
        filteredd_linklist = list(filter(lambda x: not x.startswith(self.link), link_list))
        self.external_linklist = filteredd_linklist

    def add_mail(self, mail):
        maillist.add(mail)

    def finish_crawling(self):
        self.crawled = True

    def iscrawled(self):
        return self.crawled
