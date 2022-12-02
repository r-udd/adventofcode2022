def solve_a(text):
    return sorted((map(sum, map(lambda x: map(int, x.split('\n')), text.split('\n\n')))))[-1]


def solve_b(text):
    return sum(sorted((map(sum, map(lambda x: map(int, x.split('\n')), text.split('\n\n')))))[-3:])


input_a = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''


def test_01a():
    assert solve_a(input_a) == 24000


def test_01b():
    assert solve_b(input_a) == 45000


def test_a(day01_text):
    assert solve_a(day01_text) == 68787


def test_b(day01_text):
    assert solve_b(day01_text) == 198041
