class Length:
    def __init__(self, response):
        self.string_length = len(response)

    @property
    def description(self):
        return "The length of the entire text"

    @property
    def result(self):
        return self.string_length
