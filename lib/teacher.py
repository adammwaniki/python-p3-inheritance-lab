#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        # We need to tell the code that when it's inheriting from the super, it should take the attributes of first name and last name 
        super().__init__(first_name, last_name)
        # Creating an attribute called knowledge that is now basically unique to this instance of the class because it is not present in any of its parents
        self.knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

    def teach(self):
        add_random_knowledge = random.randint(0, len(self.knowledge)-1)
        return self.knowledge[add_random_knowledge]