import yaml
from faker import Faker

def read_yaml(file_location):
    with open(file_location, 'r') as stream:
        return yaml.safe_load(stream)


def main():
    fake = Faker()
    new_yaml = read_yaml("./definition.yaml")

    customer = []

    for table in new_yaml.keys():
        print(new_yaml[table][0]['type'])


if __name__ == "__main__":
    main()
