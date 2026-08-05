
class Verbinding:
    def __init__(self, component_a, component_b, status="UNKNOWN"):

        if status not in ("UNKNOWN", "UP", "DOWN"):
            raise ValueError("Not a valid status")

        self.component_a = component_a
        self.component_b = component_b
        self.status = status



    def __str__(self):
       return f"{self.component_a.naam} <-> {self.component_b.naam} [{self.status}]"








