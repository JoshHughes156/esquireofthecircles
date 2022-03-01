
class Location:

    location_map = [] # static list of all locations in a world

    def __init__(self, name, neighbours, access=""):
        self.name = name # Descriptive name to identify location
        self.neighbours = neighbours # List of Locations that can be travelled to from the current location
        self.access = access # Allows for locking of areas until later, multiple levels can be added with space delimiters, e.g. "1 2"

    def check_access(access_level):
        return self.access in access_level

    def get_available_neighbours(access_level): # Get all neighbours that can
        return [x for x in self.neighbours if x.check_access(access_level)]
