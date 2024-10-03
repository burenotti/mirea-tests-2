import unittest
from datetime import datetime

from person import Person


class TestPerson(unittest.TestCase):

    def test_person(self):
        person = Person(
            first_name="John",
            last_name="Doe",
            middle_name="J.",
            children=[],
            birth_date=datetime(2000, 8, 14),
            death_date=datetime(2024, 3, 16),
        )

        self.assertEqual("John", person.first_name)
        self.assertEqual("Doe", person.last_name)
        self.assertEqual("J.", person.middle_name)
        self.assertEqual([], person.children)
        self.assertEqual(datetime(2000, 8, 14), person.birth_date)
        self.assertEqual(datetime(2024, 3, 16), person.death_date)

    def test_full_name(self):
        person = Person("John", "Doe", birth_date=datetime.now())
        self.assertEqual(person.full_name, "John Doe")

        person = Person("John", "Doe", middle_name="J.", birth_date=datetime.now())
        self.assertEqual(person.full_name, "John J. Doe")

    def test_age(self):
        alive_person = Person("John", "Doe", birth_date=datetime(1977, 8, 14))
        self.assertEqual(alive_person.age, 47)

        dead_person = Person(
            "John", "Doe",
            birth_date=datetime(1977, 8, 14),
            death_date=datetime(2000, 7, 13)
        )

        self.assertEqual(22, dead_person.age)

    def test_is_alive(self):
        alive_person = Person("John", "Doe", birth_date=datetime(1977, 8, 14))
        self.assertTrue(alive_person.is_alive)

        dead_person = Person(
            "John", "Doe",
            birth_date=datetime(1977, 8, 14),
            death_date=datetime(2000, 7, 13)
        )

        self.assertFalse(dead_person.is_alive)

    def test_is_child_of(self):
        bd = datetime(2000, 8, 13)
        p1 = Person("John", "Doe", birth_date=bd)
        p2 = Person("Jahn", "Doe", birth_date=bd, children=[p1])
        p3 = Person("Alex", "Doe", birth_date=bd, children=[p2])

        self.assertTrue(p1.is_child_of(p2))
        self.assertFalse(p2.is_child_of(p1))
        self.assertTrue(p1.is_child_of(p3))
