class myDict:
    def __init__(self):
        self.hashes = {}
        self.items = {}

    def __setitem__(self, key, value):
        index = len(self.hashes)
        self.hashes[index] = key
        self.items[index] = value

    def __getitem__(self, item):
        for i in range(len(self.hashes)):
            if self.hashes[i] == item:
                return self.items[i]

    def __len__(self):
        return self.__sizeof__()


dict = myDict()

dict["myDict"] = "100"
print(dict["myDict"])

