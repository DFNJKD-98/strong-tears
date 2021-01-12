class SheetRepeatException(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)


class CanNotBeEmpty(Exception):
    def __init__(self, err):
        Exception.__init__(self, err)
