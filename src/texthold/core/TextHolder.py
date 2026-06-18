from collections.abc import Iterable
from typing import BinaryIO, Self, TextIO

import setdoc
from datahold import HoldList

__all__ = ["TextHolder"]


class TextHolder(HoldList[str]):

    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable[object] = (), /) -> None:
        self._data = ()
        self.data = data

    @property
    def data(self: Self) -> tuple[str, ...]:
        "This property represents the lines of text."
        return self._data

    @data.setter
    @setdoc.basic
    def data(self: Self, value: Iterable[object], /) -> None:
        normed: tuple[str, ...]
        x: object
        normed = ()
        for x in value:
            normed += tuple(str(x).split("\n"))
        self._data = normed

    def dump(self: Self, stream: BinaryIO, /) -> None:
        "This method dumps the data into a byte stream."
        stream.write(self.dumps().encode())

    def dumpintofile(self: Self, file: str, /) -> None:
        "This method dumps the data into a file."
        item: str
        stream: TextIO
        with open(file, "w") as stream:
            for item in self:
                print(item, file=stream)

    def dumps(self: Self) -> str:
        "This method dumps the data as a string."
        ans: str
        item: str
        ans = ""
        for item in self:
            ans += item + "\n"
        return ans

    @classmethod
    def load(cls: type[Self], stream: BinaryIO, /) -> Self:
        "This classmethod loads a new instance from a given byte stream."
        return cls.loads(stream.read().decode())

    @classmethod
    def loadfromfile(cls: type[Self], file: str, /) -> Self:
        "This classmethod loads a new instance from a given file."
        stream: TextIO
        with open(file, "r") as stream:
            return cls.loads(stream.read())

    @classmethod
    def loads(cls: type[Self], string: object, /) -> Self:
        "This classmethod loads a new instance from a given string."
        text: str
        text = str(string)
        if text.endswith("\n"):
            text = text[:-1]
        return cls(text.split("\n"))
