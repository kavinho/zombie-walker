class IncorrectConfig(Exception):
    def __init__(self, config_item, message):
        self.config_item = config_item
        super().__init__(message)
