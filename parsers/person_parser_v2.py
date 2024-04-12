from dataclasses import dataclass

@dataclass
class PersonParser:
    name: str
    race: int

    def parse(self) -> str:
        return f"Hello my name is {self.name} and I'm a {self.race}"

def initialize(factory) -> None:
    factory.register("v2", PersonParser)