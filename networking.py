import uuid, os

data: bytes = uuid.uuid4().bytes
if os.path.isfile("./data"):
    with open("./data", "rb") as file:
        data = file.read(16)
else:
    with open("./data", "wb") as file:
        file.write(uuid.uuid4().bytes)
print(data)


class Networking:
    def __init__(self, pseudo: str) -> None:
        assert isinstance(pseudo, str)
        self.pseudo: str = pseudo
        self.__uuid = uuid.uuid4()
        pass
