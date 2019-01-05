class LengthWithoutSpaces:
    def __init__(self, response):
        self.string_length = len(response.replace(" ", ""))

    @property
    def description(self):
        return "The length of the entire text without spaces"

    @property
    def result(self):
        return self.string_length
