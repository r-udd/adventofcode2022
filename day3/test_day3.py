score = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def solve_a_line(rucksack):
    comp2 = rucksack[len(rucksack)//2:]
    for letter in rucksack[:len(rucksack)//2]:
        if letter in comp2:
            return score.index(letter)


def solve_a(rucksack):
    return sum(map(solve_a_line, rucksack))


def solve_group(group):
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return score.index(letter)


def solve_b(rucksacks):
    s = 0
    for i in range(0, len(rucksacks), 3):
        s += solve_group(rucksacks[i:i+3])
    return s


input_a = 'vJrwpWtwJgWrhcsFMMfFFhFp'
input_b = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
input_c = 'PmmdzqPrVvPwwTWBwg'
input_d = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
input_e = 'ttgJtRGJQctTZtZT'
input_f = 'CrZsJsPPZsGzwwsLwLmpwMDw'
input_2a = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg']
input_2b = ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']


def test_1a():
    assert solve_a_line(input_a) == 16


def test_1b():
    assert solve_a_line(input_b) == 38


def test_1c():
    assert solve_a_line(input_c) == 42


def test_1d():
    assert solve_a_line(input_d) == 22


def test_1e():
    assert solve_a_line(input_e) == 20


def test_1f():
    assert solve_a_line(input_f) == 19


def test_2a():
    assert solve_group(input_2a) == 18


def test_2b():
    assert solve_group(input_2b) == 52


def test_2c():
    assert solve_b(input_2a + input_2b) == 70


def test_1(day03_lines):
    assert solve_a(day03_lines) == 8240


def test_2(day03_lines):
    assert solve_b(day03_lines) == 2587