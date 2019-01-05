class Lines:
    def __init__(self, response):
        self.line_count = len(response.split("\n"))

    @property
    def description(self):
        return "Lines"

    @property
    def result(self):
        return self.line_count
