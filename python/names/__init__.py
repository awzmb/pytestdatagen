from os.path import abspath, join, dirname
import random

def generate_name():
    return f"{get_first_name()} {get_last_name()}"


def get_first_name():
  return random.choice(open('names.first').readlines())


def get_last_name():
  return random.choice(open('names.last').readlines())


def main():
  print(generate_name())


if __name__ == "__main__":
  main()
