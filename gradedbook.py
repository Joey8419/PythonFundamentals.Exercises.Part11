from enum import Enum


class AliveStatus(Enum):
    # Enum class with two symbolic names
    Deceased = 0
    Alive = 1


class Person:

    def __int__(self, first_name, last_name, dob, alive_status):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive_status = alive_status

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_alive_status(self, alive_status):
        self.alive_status = alive_status
