class Person:
    def __init__(self, brain, heart, leg):
        self.brain = brain
        self.heart = heart
        self.leg = leg

class Heart:
    def __init__(self, cardiac_output):
        self.cardiac_output = cardiac_output

    @property
    def state(self):
        if self.cardiac_output > 70:
            return "high blood pressure"
        else:
            return "feeling good"

class Brain:
    def __init__(self, brain_load):
        self.brain_load = brain_load

    @property
    def state(self):
        if self.brain_load > 90:
            return "tired"
        else:
            return "rested"

class Leg:
    def __init__(self, person, moving_speed, frofferty):
        self.person = person
        self.moving_speed = moving_speed
        self.frofferty = frofferty

    @property
    def state(self):
        if self.moving_speed > 10:
            return "running"
        else:
            return "walking" if self.frofferty == "walking" else "standing"
