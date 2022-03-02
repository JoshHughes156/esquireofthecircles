
class Location:

    def __init__(self, name, access="", npcs=list()):
        self.name = name # Descriptive name to identify location
        self.access = access # Allows for locking of areas until later, multiple levels can be added with space delimiters, e.g. "1 2"

    def check_access(self, access_level):
        return self.access in access_level

    def get_neighbours(self, access_level=""): # Get all neighbours that can
        return [x for x in self.neighbours if x.check_access(access_level)]

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours # List of Locations that can be travelled to from the current location

