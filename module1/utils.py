import first_test


def cli_color(string, new=0, end=0, color='g'):
    colors = {
        'g': '[032m',
        'r': '[031m',
        'w': '[0m',
    }
    str = chr(27) + colors[color] + string + chr(27) + colors['w']
    if (new):
        str = '\n' + str
    if (end):
        str += '\n'
    return str


def test(received, expected):
    if (expected == received):
        print(cli_color("OK", 0, 1))
    else:
        print(cli_color("Fail", 0, 1, 'r'))


def test_my_sum():
    print("We are testing my_sum!" + '\n')
    test(12, first_test.my_sum((10, 2, 0)))
    test(144, first_test.my_sum((10, 20, 100, 14)))
    test(12, first_test.my_sum((-50, 200, -100, -50, 12)))


def test_shortener():
    print("We are testing shortener!" + '\n')
    sourceStrings = (
        'A very looooooong wooooord',
        'Loremia ipsumia dolaria sitia ameti',
        'Have you ever been to Lituania ?',
        'Anyone who reads Old and Middle',
        'English literary texts will be familiar',
        'with the mid-brown volumes of the EETS,',
        'with the symbol of Alfreds jewel embossed on the front cover+'
    )

    testStrings = (
        'A very looooo* wooooo*',
        'Loremi* ipsumi* dolari* sitia ameti',
        'Have you ever been to Lituan* ?',
        'Anyone who reads Old and Middle',
        'Englis* litera* texts will be famili*',
        'with the mid-br* volume* of the EETS,',
        'with the symbol of Alfred* jewel emboss* on the front cover+'
    )

    for i in range(len(sourceStrings)):
        test(testStrings[i], first_test.shortener(sourceStrings[i]))


def test_compare_ends():
    print("We are testing compare_ends!" + '\n')
    test(first_test.compare_ends(('aba', 'xyz', 'aa', 'x', 'bbb')), 3)
    test(first_test.compare_ends(('', 'x', 'xy', 'xyx', 'xx')), 2)
    test(first_test.compare_ends(('aaa', 'be', 'abc', 'hello')), 1)


def test_spam():
    print("We are testing spam!" + '\n')
    test(first_test.spam((3)), 'bulochka'*3)
    test(first_test.spam((1)), 'bulochka')
    test(first_test.spam((8)), 'bulochka'*8)


test_spam()

test_shortener()

test_compare_ends()

test_my_sum()
