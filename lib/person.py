#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = 'Guido', job = 'Sales' ):
        self.name = name
        self.job = job
    def get_job(self):
        return self._job
    def set_job(self,job):
        if(isinstance(job,str) and job in APPROVED_JOBS):
            self._job = job
        else:
            print ("Job must be in list of approved jobs.")
    job = property(get_job, set_job)
    def set_name(self, name):
        if(isinstance(name,str) and (1 <= len(name) <= 25)):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_name(self):
        return self._name
    name = property(get_name, set_name)

# class Human:
#     species = "Homo sapiens"
#     def get_age(self):
#         print("Retrieving age.")
#         return self._age
#     def set_age(self, age):
#         if (type(age) in (int, float)) and (0 <= age <= 120):
#             print(f"Setting age to { age }.")
#             self._age = age
#         else:
#             print("Age must be a number between 0 and 120.")
#     age = property(get_age, set_age,)