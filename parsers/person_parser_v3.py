from dataclasses import dataclass

@dataclass
class PersonParser:
    name: str
    race: int
    alignment: str  # new field added to PersonParser class

    def parse(self) -> str:
        return f"Hello my name is {self.name} and I'm a {self.race} and my alignment is {self.alignment}"

def initialize(factory) -> None:
    factory.register("v3", PersonParser)
