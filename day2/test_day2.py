def solve_a(rounds):
    results = {'A': {'X': 4, 'Y': 8, 'Z': 3},
               'B': {'X': 1, 'Y': 5, 'Z': 9},
               'C': {'X': 7, 'Y': 2, 'Z': 6}}
    return sum(map(lambda round: results[round[0]][round[1]], rounds))


def solve_b(rounds):
    results = {'A': {'X': 3, 'Y': 4, 'Z': 8},
               'B': {'X': 1, 'Y': 5, 'Z': 9},
               'C': {'X': 2, 'Y': 6, 'Z': 7}}
    return sum(map(lambda round: results[round[0]][round[1]], rounds))


input_a = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


def test_01a():
    assert solve_a(input_a) == 15


def test_01b():
    assert solve_b(input_a) == 12


def test_a(day02_grid):
    assert solve_a(day02_grid) == 9651


def test_b(day02_grid):
    assert solve_b(day02_grid) == 10560
