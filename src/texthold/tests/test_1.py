import io
import os
import unittest
from typing import *

from texthold.core import TextHolder

__all__ = ["TestHolder"]


class TestHolder(unittest.TestCase):

    def setUp(self: Self) -> None:
        "This setup initializes a Holder instance for testing."
        self.holder = TextHolder(["Hello", "World"])

    def test_data_property_getter(self: Self) -> None:
        "This test tests the data property getter."
        self.assertEqual(self.holder.data, ["Hello", "World"])

    def test_data_property_setter(self: Self) -> None:
        "This test tests the data property setter."
        self.holder.data = ["New", "Data"]
        self.assertEqual(self.holder.data, ["New", "Data"])

    def test_data_property_setter_multiline(self: Self) -> None:
        "This test tests setting multiline strings."
        self.holder.data = ["First\nSecond", "Third"]
        self.assertEqual(self.holder.data, ["First", "Second", "Third"])

    def test_data_property_deleter(self: Self) -> None:
        "This test tests deleting the data property."
        with self.assertRaises(Exception):
            del self.holder.data

    def test_dumps(self: Self) -> None:
        "This test tests the dumps method."
        self.assertEqual(self.holder.dumps(), "Hello\nWorld\n")

    def test_dump(self: Self) -> None:
        "This test tests the dump method with a binary stream."
        stream: io.BytesIO
        stream = io.BytesIO()
        self.holder.dump(stream)
        self.assertEqual(stream.getvalue().decode(), "Hello\nWorld\n")

    def test_load(self: Self) -> None:
        "This test tests the load method from a binary stream."
        loaded_holder: TextHolder
        stream: io.BytesIO
        stream = io.BytesIO(b"Test\nLoad\n")
        loaded_holder = TextHolder.load(stream)
        self.assertEqual(loaded_holder.data, ["Test", "Load"])

    def test_loads(self: Self) -> None:
        "This test tests the loads method."
        loaded_holder: TextHolder
        loaded_holder = TextHolder.loads("Test\nLoad\n")
        self.assertEqual(loaded_holder.data, ["Test", "Load"])

    def test_dumpintofile_and_loadfromfile(self: Self) -> None:
        "This test tests dumping to and loading from a file."
        filename: str
        loaded_holder: TextHolder
        filename = "test_holder.txt"
        self.holder.dumpintofile(filename)
        loaded_holder = TextHolder.loadfromfile(filename)
        self.assertEqual(loaded_holder.data, self.holder.data)
        os.remove(filename)

    def test_empty_initialization(self: Self) -> None:
        "This test tests initializing Holder with no data."
        empty_holder: TextHolder
        empty_holder = TextHolder([])
        self.assertEqual(empty_holder.data, [])

    def test_mixed_type_input(self: Self) -> None:
        "This test tests initializing Holder with mixed-type input."
        mixed_holder: TextHolder
        mixed_holder = TextHolder(["String", 123, 45.67])
        self.assertEqual(mixed_holder.data, ["String", "123", "45.67"])

    def test_multiline_string_input(self: Self) -> None:
        "This test tests initializing Holder with multiline strings."
        multiline_holder: TextHolder
        multiline_holder = TextHolder(["Line1\nLine2", "Line3"])
        self.assertEqual(multiline_holder.data, ["Line1", "Line2", "Line3"])


if __name__ == "__main__":
    unittest.main()
