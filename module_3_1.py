calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    l = len(string)
    u = string.upper()
    lo = string.lower()
    return (l, u, lo)


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    return (string in
            [item.lower() for item in list_to_search])


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',
                  ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle',
                  ['recycling', 'cyclic']))  # No matches
print(calls)
