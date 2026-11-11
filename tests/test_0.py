from __future__ import annotations

__all__: list[str] = ["TestHolder"]


import tempfile
import unittest
from io import BytesIO, TextIOWrapper
from pathlib import Path
from typing import Any, Self

from texthold.core.TextHolder import TextHolder


class TestHolder(unittest.TestCase):

    def test_data_property(self: Self, /) -> None:
        holder: TextHolder
        holder = TextHolder(["line1", "line2"])
        self.assertEqual(holder.data, ("line1", "line2"))
        holder.data = ["new line1\nnew line2", "line3"]
        self.assertEqual(holder.data, ("new line1", "new line2", "line3"))

    def test_del(self: Self, /) -> None:
        holder: TextHolder
        holder = TextHolder(["new line1", "new line2", "line3"])
        with self.assertRaises(Exception):
            del holder.data
        self.assertEqual(holder.data, ("new line1", "new line2", "line3"))

    def test_dumps(self: Self, /) -> None:
        holder: TextHolder
        result: Any
        holder = TextHolder(["line1", "line2"])
        result = holder.dumps()
        self.assertEqual(result, "line1\nline2\n")

    def test_load(self: Self, /) -> None:
        holder: TextHolder
        stream: BytesIO
        stream = BytesIO(b"line1\nline2\n")
        holder = TextHolder.load(stream)
        self.assertEqual(holder.data, ("line1", "line2"))

    def test_dumpintofile_and_loadfromfile(self: Self, /) -> None:
        content: Any
        holder: TextHolder
        loaded_holder: TextHolder
        stream: TextIOWrapper
        tmp: str
        tmp_dir: Path
        tmp_file: Path
        holder = TextHolder(["line1", "line2"])
        with tempfile.TemporaryDirectory() as tmp:
            tmp_dir = Path(tmp)
            tmp_file = tmp_dir / "a"
            holder.dumpintofile(str(tmp_file))
            with open(str(tmp_file), "r") as stream:
                content = stream.read()
                self.assertEqual(content, "line1\nline2\n")
            loaded_holder = TextHolder.loadfromfile(str(tmp_file))
            self.assertEqual(loaded_holder.data, ("line1", "line2"))

    def test_loads(self: Self, /) -> None:
        holder: TextHolder
        string: str
        string = "line1\nline2\n"
        holder = TextHolder.loads(string)
        self.assertEqual(holder.data, ("line1", "line2"))


if __name__ == "__main__":
    unittest.main()
