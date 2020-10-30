import unittest

from enums.Sex import Sex
from main.Human import Human


class TestHuman(unittest.TestCase):
    male_ssn = "1 98 06 78 123 456 78"
    female_ssn = "2 85 11 92 12 345 678"

    def test_one_human(self):
        one_human = Human(self.male_ssn)
        self.assertEqual(one_human.social_security_number, self.male_ssn)

    def test_one_male(self):
        one_male = Human(self.male_ssn)
        self.assertEqual(one_male.sex, Sex.MALE)

    def test_one_female(self):
        one_female = Human(self.female_ssn)
        self.assertEqual(one_female.sex, Sex.FEMALE)

    def test_year_of_birth(self):
        one_human_born_in_98 = Human(self.male_ssn)
        self.assertEqual(one_human_born_in_98.year_of_birth, "1998")

    def test_month_of_birth(self):
        one_human_born_in_november = Human(self.female_ssn)
        self.assertEqual(one_human_born_in_november.month_of_birth, "11")

    def test_place_of_birth(self):
        one_human_born_in_paris = Human(self.male_ssn)
        self.assertEqual(one_human_born_in_paris.place_of_birth, "78")


if __name__ == '__main__':
    unittest.main()
