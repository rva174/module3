calls = 0

def count_calls():
    global calls

    calls += 1

def string_info(string):
    string = ('Urban')
    string_info = (len(string), [string.upper(), string.lower()])
    print(string_info)


    count_calls()

    return string



def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [value.lower() for value in list_to_search]

    count_calls()

    return string in list_to_search

#print(string_info('Capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
