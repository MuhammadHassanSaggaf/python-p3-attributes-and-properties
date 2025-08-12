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
    def __init__(self, name="guido", job="ITC"):
        self.set_name(name)
        self.set_job(job)

    def set_name(self, name):
        if (type(name) is str and 1 <= len(name) <= 25):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")