import yaml
from faker import Faker

def read_yaml(file_location):
    with open(file_location, 'r') as stream:
        parsed_yaml=yaml.safe_load(stream)
        print(parsed_yaml)
        return parsed_yaml


def main():
    fake = Faker()
    print(fake.address())
    read_yaml("./test.yaml")


if __name__ == "__main__":
    main()
