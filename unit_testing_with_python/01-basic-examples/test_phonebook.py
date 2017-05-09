import unittest

from phonebook import Phonebook

class PhoneBookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))

    def test_missing_entry_raises_KeyError(self):
        self.phonebook = Phonebook()

        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.phonebook = Phonebook()
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("This is poor unittest design")
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "12345") # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())
        self.phonebook.add("Sue", "123")  # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consitent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsitent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "12345")  # identical to Bob
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_with_same_prefix_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Sue", "123")  # prefix of Bob
        self.assertFalse(self.phonebook.is_consistent())