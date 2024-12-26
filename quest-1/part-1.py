def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def solution(lines: list[str]):
    notes = lines[0]

    total_potions = 0
    for creature in notes:
        if creature == 'B':
            total_potions += 1
        elif creature == 'C':
            total_potions += 3
        else:
            continue
    
    print(total_potions)


lines = read_input_file(file_path="input_1.txt")
solution(lines)