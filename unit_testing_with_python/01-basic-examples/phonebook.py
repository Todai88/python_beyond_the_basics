class Phonebook:

    def __init__(self):
        self._entries = {}

    def add(self, name, number):
        self._entries[name] = number

    def lookup(self, name):
        return self._entries[name]

    def is_consistent(self):
        if not self._entries:
            return True
        else:
            if self.check_duplicate():
                if self.check_prefix():
                    return True
        return False

    def check_duplicate(self):
        seen = set()
        for x in self.get_values():
            if x not in seen:
                seen.add(x)
            else:
                return False
        return True

    def check_prefix(self):
        prefixes = []
        for contact_number in self.get_values():
            if contact_number not in map(lambda number: number[0:len(contact_number)], prefixes):
                prefixes.append(contact_number)
            else:
                return False
        return True

    def get_values(self):
        return self._entries.values()