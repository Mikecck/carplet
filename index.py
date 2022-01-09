class Index:
    def __init__(self, id_str: str, init_value: int) -> None:
        if id_str == "":
            raise NameError("Index id cannot be empty string")
        self._id_str = id_str

        if init_value <= 0:
            raise ValueError("Index initial value cannot be negative or zero")
        self._value = init_value

    @property
    def id_str(self):
        return self._id_str
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, d: int):
        self._value += d

    def reset(self, value):
        self._value = value
    
    def destroy(self) -> bool:
        return self._value <= 0


    