from datetime import datetime

class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }


class Scan:
    def __init__(self, email: str, child: Child, image_name: str, predictions: dict, date: datetime):
        self.email = email
        self.child = child
        self.image_name = image_name
        self.predictions = predictions
        self.date = date

    def to_dict(self):
        return {
            "email": self.email,
            "child_name": self.child.name,
            "age": self.child.age,
            "image_name": self.image_name,
            "predictions": self.predictions,
            "date": self.date
        }


class Visit:
    def __init__(self, email: str, visit_date: datetime, reason: str):
        self.email = email
        self.visit_date = visit_date
        self.reason = reason

    def to_dict(self):
        return {
            "email": self.email,
            "visit_date": self.visit_date,
            "reason": self.reason
        }


class HygieneReport:
    def __init__(self, email: str, child_name: str, date: str, brushed: bool, flossed: bool):
        self.email = email
        self.child_name = child_name
        self.date = date
        self.brushed = brushed
        self.flossed = flossed

    def to_dict(self):
        return {
            "email": self.email,
            "child_name": self.child_name,
            "date": self.date,
            "brushed": self.brushed,
            "flossed": self.flossed
        }


class UserSession:
    def __init__(self, email: str):
        self.email = email

    def to_dict(self):
        return {
            "email": self.email
        }
