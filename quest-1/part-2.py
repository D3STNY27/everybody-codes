import os
os.system('cls')


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


def get_required_potions(creature_a: str, creature_b: str | None = None):
    if creature_b is None:
        return POTIONS_MAP[creature_a]

    return POTIONS_MAP[creature_a] + POTIONS_MAP[creature_b] + 2


def solution(lines: list[str]):
    notes = lines[0]

    total_potions = 0
    for i in range(0, len(notes), 2):
        creature_a, creature_b = notes[i], notes[i+1]
        
        if creature_a == 'x' and creature_b == 'x':
            continue

        if creature_a == 'x':
            potions = get_required_potions(creature_a=creature_b)
        elif creature_b == 'x':
            potions = get_required_potions(creature_a=creature_a)
        else:
            potions = get_required_potions(creature_a=creature_a, creature_b=creature_b)
        
        total_potions += potions
    
    print(total_potions)


lines = read_input_file(file_path="input_2.txt")
solution(lines)