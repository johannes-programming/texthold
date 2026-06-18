import io
import os
import tempfile
import unittest
from typing import Any, Self

from texthold.core.TextHolder import TextHolder

__all__ = ["TestHolder"]


class TestHolder(unittest.TestCase):

    def test_data_property_getter(self: Self) -> None:
        "This test tests the data property getter."
        holder: TextHolder
        holder = TextHolder(["Hello", "World"])
        self.assertEqual(holder.data, ("Hello", "World"))

    def test_data_property_setter(self: Self) -> None:
        "This test tests the data property setter."
        holder: TextHolder
        holder = TextHolder(["Hello", "World"])
        holder.data = ["New", "Data"]
        self.assertEqual(holder.data, ("New", "Data"))

    def test_data_property_setter_multiline(self: Self) -> None:
        "This test tests setting multiline strings."
        holder: TextHolder
        holder = TextHolder(["Hello", "World"])
        holder.data = ["First\nSecond", "Third"]
        self.assertEqual(holder.data, ("First", "Second", "Third"))

    def test_data_property_deleter(self: Self) -> None:
        "This test tests deleting the data property."
        holder: TextHolder
        holder = TextHolder(["Hello", "World"])
        with self.assertRaises(Exception):
            del holder.data

    def test_dumps(self: Self) -> None:
        "This test tests the dumps method."
        holder: TextHolder
        holder = TextHolder(["Hello", "World"])
        self.assertEqual(holder.dumps(), "Hello\nWorld\n")

    def test_dump(self: Self) -> None:
        "This test tests the dump method with a binary stream."
        holder: TextHolder
        stream: io.BytesIO
        holder = TextHolder(["Hello", "World"])
        stream = io.BytesIO()
        holder.dump(stream)
        self.assertEqual(stream.getvalue().decode(), "Hello\nWorld\n")

    def test_load(self: Self) -> None:
        "This test tests the load method from a binary stream."
        loaded_holder: TextHolder
        stream: io.BytesIO
        stream = io.BytesIO(b"Test\nLoad\n")
        loaded_holder = TextHolder.load(stream)
        self.assertEqual(loaded_holder.data, ("Test", "Load"))

    def test_loads(self: Self) -> None:
        "This test tests the loads method."
        loaded_holder: TextHolder
        loaded_holder = TextHolder.loads("Test\nLoad\n")
        self.assertEqual(loaded_holder.data, ("Test", "Load"))

    def test_dumpintofile_and_loadfromfile(self: Self) -> None:
        "This test tests dumping to and loading from a file."
        file: str
        filename: str
        holder: TextHolder
        loaded_holder: TextHolder
        tmpdir: Any
        filename = "test_holder.txt"
        holder = TextHolder(["Hello", "World"])
        with tempfile.TemporaryDirectory() as tmpdir:
            file = os.path.join(tmpdir, filename)
            holder.dumpintofile(file)
            loaded_holder = TextHolder.loadfromfile(file)
        self.assertEqual(loaded_holder.data, holder.data)

    def test_empty_initialization(self: Self) -> None:
        "This test tests initializing Holder with no data."
        empty_holder: TextHolder
        empty_holder = TextHolder([])
        self.assertEqual(empty_holder.data, ())

    def test_mixed_type_input(self: Self) -> None:
        "This test tests initializing Holder with mixed-type input."
        mixed_holder: TextHolder
        mixed_holder = TextHolder(["String", 123, 45.67])
        self.assertEqual(mixed_holder.data, ("String", "123", "45.67"))

    def test_multiline_string_input(self: Self) -> None:
        "This test tests initializing Holder with multiline strings."
        multiline_holder: TextHolder
        multiline_holder = TextHolder(["Line1\nLine2", "Line3"])
        self.assertEqual(multiline_holder.data, ("Line1", "Line2", "Line3"))

    def test_bool(self: Self) -> None:
        "This test tests initializing Holder with multiline strings."
        holder: TextHolder
        holder = TextHolder(["Line1\nLine2", "Line3"])
        self.assertTrue(bool(holder))
        holder.clear()
        self.assertFalse(bool(holder))
        holder.append("hello")
        self.assertTrue(bool(holder))
        holder = TextHolder()
        self.assertFalse(bool(holder))

    def test_repr(self: Self) -> None:
        "This test tests initializing Holder with multiline strings."
        holder: TextHolder
        holder = TextHolder(["Line1\nLine2", "Line3"])
        self.assertTrue(repr(holder).startswith("TextHolder(["))
        self.assertEqual(repr(holder), str(holder))


if __name__ == "__main__":
    unittest.main()
