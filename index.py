class Index:
    def __init__(self, id_str: str, init_value: int) -> None:
        if id_str == "":
            raise NameError("Index id cannot be empty string")
        self._id_str = id_str

        if init_value <= 0:
            raise ValueError("Index initial value cannot be negative or zero")
        self._init_value = init_value

    @property
    def id_str(self):
        return self._id_str
    
    @property
    def init_value(self):
        return self.init_value
    
    @init_value.setter
    def init_value(self, d):
        self._init_value += d
    
    def destroy(self) -> bool:
        return self._init_value <= 0


    