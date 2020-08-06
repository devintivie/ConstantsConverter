
class ConstantPrint(dict):
    def __init__(self, *args, **kwargs):
        super(ConstantPrint, self).__init__(*args, **kwargs)
        self.__dict__ = self