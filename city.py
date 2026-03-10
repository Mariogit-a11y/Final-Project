class City:
    def __init__(self, city_name, state):
        self.city_name = city_name
        self.state = state
#
    def __repr__(self):
        return f"{self.city_name}, {self.state}"

    def __eq__(self, other):
        return (self is other or
                type(other) == City and
                self.city_name == other.city_name and
                self.state == other.state)