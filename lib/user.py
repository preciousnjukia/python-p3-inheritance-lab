#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def given_name(self):
        return f"{self.first_name}"
    
    def family_name(self):
        return f"{self.last_name}"






user = User("John", "Doe")
user.given_name = "John"
user.family_name = "Doe"