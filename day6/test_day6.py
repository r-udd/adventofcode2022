def solve(signal, length):
    for i in range(length, len(signal)):
        if len(set(signal[i-length:i])) == length:
            return i


def solve_a(signal):
    return solve(signal, 4)


def solve_b(signal):
    return solve(signal, 14)


input_a = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
input_b = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
input_c = 'nppdvjthqldpwncqszvftbrmjlhg'
input_d = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
input_e = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


def test_1a():
    assert solve_a(input_a) == 7


def test_1b():
    assert solve_a(input_b) == 5


def test_1c():
    assert solve_a(input_c) == 6


def test_1d():
    assert solve_a(input_d) == 10


def test_1e():
    assert solve_a(input_e) == 11


def test_2a():
    assert solve_b(input_a) == 19


def test_2b():
    assert solve_b(input_b) == 23


def test_2c():
    assert solve_b(input_c) == 23


def test_2d():
    assert solve_b(input_d) == 29


def test_2e():
    assert solve_b(input_e) == 26


def test_1(day06_text):
    assert solve_a(day06_text) == 1175


def test_2(day06_text):
    assert solve_b(day06_text) == 3217
