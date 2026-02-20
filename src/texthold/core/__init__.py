from typing import *

import cmp3
import setdoc
from datahold import HoldList
from datarepr import datarepr

__all__ = ["TextHolder"]


class TextHolder(cmp3.CmpABC, HoldList[str]):

    data: tuple[str, ...]

    __slots__ = ()

    @setdoc.basic
    def __bool__(self: Self) -> bool:
        return bool(self._data)

    @setdoc.basic
    def __cmp__(self: Self, other: Any) -> Any:
        return cmp3.cmp(self._data, tuple(other), mode="le")

    @setdoc.basic
    def __format__(self: Self, format_spec: Any = "", /) -> str:
        return format(self._data, str(format_spec))

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, list(self))

    @setdoc.basic
    def __str__(self: Self) -> str:
        return repr(self)

    @property
    def data(self: Self) -> list[str]:
        "This property represents the lines of text."
        return list(self._data)

    @data.setter
    def data(self: Self, value: Iterable, /) -> None:
        normed: list
        x: Any
        normed = list()
        for x in value:
            normed += str(x).split("\n")
        self._data = normed

    def dump(self: Self, stream: BinaryIO) -> None:
        "This method dumps the data into a byte stream."
        stream.write(self.dumps().encode())

    def dumpintofile(self: Self, file: Any) -> None:
        "This method dumps the data into a file."
        item: Any
        stream: Any
        with open(file, "w") as stream:
            for item in self:
                print(item, file=stream)

    def dumps(self: Self) -> str:
        "This method dumps the data as a string."
        return "\n".join(self._data) + "\n"

    @classmethod
    def load(cls: type, stream: BinaryIO) -> Self:
        "This classmethod loads a new instance from a given byte stream."
        return cls.loads(stream.read().decode())

    @classmethod
    def loadfromfile(cls: type, file: Any) -> Self:
        "This classmethod loads a new instance from a given file."
        stream: Any
        with open(file, "r") as stream:
            return cls.loads(stream.read())

    @classmethod
    def loads(cls: type, string: Any) -> Self:
        "This classmethod loads a new instance from a given string."
        text: str
        text = str(string)
        if text.endswith("\n"):
            text = text[:-1]
        return cls(text.split("\n"))
