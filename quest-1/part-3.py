import os
os.system('cls')


CREATURE_GROUP_SIZE = 3

POTIONS_MAP = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5
}


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def get_required_potions(creatures: list[str]):
    return sum([POTIONS_MAP[creature] + (len(creatures)-1) for creature in creatures])


def solution(lines: list[str]):
    notes = lines[0]

    total_potions = 0
    for i in range(0, len(notes), CREATURE_GROUP_SIZE):
        creatures = [creature for creature in notes[i:i+CREATURE_GROUP_SIZE] if creature != 'x']
        total_potions += get_required_potions(creatures=creatures)
    
    print(total_potions)


lines = read_input_file(file_path="input_3.txt")
solution(lines)