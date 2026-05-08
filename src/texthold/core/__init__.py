from typing import *

from datahold import OkayList

__all__ = ["Holder"]


class Holder(OkayList):
    @property
    def data(self) -> list[str]:
        "This property represents the lines of text."
        return list(self._data)

    @data.setter
    def data(self, value: Iterable, /) -> None:
        normed = list()
        for x in value:
            normed += str(x).split("\n")
        self._data = normed

    @data.deleter
    def data(self) -> None:
        self._data = list()

    def dump(self, stream: BinaryIO) -> None:
        "This method dumps the data into a byte stream."
        stream.write(self.dumps().encode())

    def dumpintofile(self, file: Any) -> None:
        "This method dumps the data into a file."
        with open(file, "w") as stream:
            for item in self:
                print(item, file=stream)

    def dumps(self) -> str:
        "This method dumps the data as a string."
        return "\n".join(self._data) + "\n"

    @classmethod
    def load(cls, stream: BinaryIO) -> Self:
        "This classmethod loads a new instance from a given byte stream."
        return cls.loads(stream.read().decode())

    @classmethod
    def loadfromfile(cls, file: Any) -> Self:
        "This classmethod loads a new instance from a given file."
        with open(file, "r") as stream:
            return cls.loads(stream.read())

    @classmethod
    def loads(cls, string: str) -> Self:
        "This classmethod loads a new instance from a given string."
        if string.endswith("\n"):
            string = string[:-1]
        data = string.split("\n")
        return cls(data)
