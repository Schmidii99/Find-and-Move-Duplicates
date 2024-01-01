import hashlib
import os


class MyFile:
    def __init__(self, name, path, file_size, file_hash):
        self.name = name
        self.path = path
        self.file_size = file_size
        self.file_hash = file_hash

    @staticmethod
    def from_path(file_path) -> "MyFile":
        file_hash = hashlib.md5((open(file_path, "rb").read())).hexdigest()
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        return MyFile(file_name, file_path, file_size, file_hash)

    def __eq__(self, other) -> bool:
        if isinstance(other, MyFile):
            if self.name != other.name:
                return False
            if self.file_size != other.file_size:
                return False
            if self.file_hash != other.file_hash:
                return False
            return True
        else:
            return False
