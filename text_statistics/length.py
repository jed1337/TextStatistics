class Length:
    def __init__(self, response):
        self.response = response
        self.string_length = self._get_length()

    def _get_length(self):
        string_length = 0
        for line in self.response:
            string_length += len(line)

        return string_length

    @property
    def description(self):
        return "The length of the entire text"

    @property
    def result(self):
        return self.string_length
