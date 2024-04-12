from dataclasses import dataclass

@dataclass
class PersonParser:
    name: str

    def parse(self) -> str:
        return f"Hello my name is {self.name}"

def initialize(factory) -> None:
    factory.register("v1", PersonParser)