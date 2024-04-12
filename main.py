import os
import factory
import loader
import json

config_path = os.path.join(os.path.dirname(__file__), "config.json")
with open(config_path) as config_json:
    config = json.load(config_json)

def get_files_to_parse() -> list[str]:
    data_path = os.path.join(os.path.dirname(__file__), "data")
    for dirpath, _, filenames in os.walk(data_path):
        return [os.path.join(dirpath, filename) for filename in filenames]


def main() -> None:
    # Load plugins
    loader.load_plugins(config["parsers"])

    for file in get_files_to_parse():
        with open(file) as data_file:
            data = json.load(data_file)

        for item in data:
            parser = factory.create({"type": item["version"], "data": item["data"]})
            print(parser.parse())

if __name__ == "__main__":
    main()