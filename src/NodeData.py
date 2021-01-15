

class Node(object):

    def __init__(self,key, geo_location: tuple = None):
        self.key = key
        self.info = ""
        self.tag = 0
        self.weight = 0
        self.geo_location = geo_location

    def node(self, node_data):
        self.key = node_data.get_key
        self.info = node_data.get_info
        self.tag = node_data.get_tag
        self.weight = node_data.get_weight
        self.set_location(node_data.get_location)

    def node(self, key, geo_location: tuple = None):
        self.key = key
        self.info = ''
        self.tag = 0
        self.weight = 0
        self.geo_location = geo_location

    def node(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def get_location(self):
        return self.geo_location

    def set_location(self, geo1, geo2, geo3):
        self.geo_location = (geo1, geo2, geo3)

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_info(self):
        return self.info

    def set_info(self, string):
        self.info=string

    def get_tag(self):
        return self.tag

    def set_tag(self, tag):
        self.tag = tag













