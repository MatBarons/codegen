class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._data = {}
        return cls._instance

    def set(self, key, value):
        self._data[key] = value

    def get(self, key, default=None):
        return self._data.get(key, default)

    def remove(self, key):
        if key in self._data:
            del self._data[key]

    def get_all(self):
        return self._data.copy()

    def clear(self):
        self._data.clear()