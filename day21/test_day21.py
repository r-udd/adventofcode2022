import operator


def solve_a(current, all):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    value = all[current]
    if isinstance(value, int):
        return value
    else:
        return operators[value[1]](solve_a(value[0], all), solve_a(value[2], all))


def parse(text):
    result = {}
    for line in text:
        key, rest = line.split(': ')
        if rest.isdigit():
            result[key] = int(rest)
        else:
            result[key] = [rest[:4], rest[5], rest[-4:]]
    return result


def test_parse_int():
    assert parse(['root: 4']) == {'root': 4}


def test_parse_text():
    assert parse(['root: sllz + lgvd']) == {'root': ['sllz', '+', 'lgvd']}


def test_solve_int():
    assert solve_a('root', {'root': 4}) == 4


def test_solve_plus():
    assert solve_a('root', {'root': ['aaaa', '+', 'bbbb'], 'aaaa': 3, 'bbbb': 5}) == 8


def solve_b(signal):
    return solve_a(signal, 14)


input_a = ['root: pppw + sjmn',
           'dbpl: 5',
           'cczh: sllz + lgvd',
           'zczc: 2',
           'ptdq: humn - dvpt',
           'dvpt: 3',
           'lfqf: 4',
           'humn: 5',
           'ljgn: 2',
           'sjmn: drzm * dbpl',
           'sllz: 4',
           'pppw: cczh / lfqf',
           'lgvd: ljgn * ptdq',
           'drzm: hmdt - zczc',
           'hmdt: 32']


def test_1a():
    d = parse(input_a)
    assert solve_a('root', d) == 152


def test_1(day21_lines):
    d = parse(day21_lines)
    assert solve_a('root', d) == 158661812617812


def test_2(day21_lines):
    assert solve_b(day21_lines) == 3217
