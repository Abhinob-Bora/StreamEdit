# from server import mongo  # Import the MongoDB instance

class Overlay:
    def __init__(self, name, position, size, content):
        self.name = name
        self.position = position
        self.size = size
        self.content = content

    def save(self):
        # Implement code to save overlay to the database
        pass

    @staticmethod
    def find_by_name(name):
        # Implement code to find overlay by name in the database
        pass

    # Implement other CRUD methods as needed
