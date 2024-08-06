calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_info = (len(string), string.upper(), string.lower())
    print(string_info)

    count_calls()
    return string_info

def is_contains(string, list_to_search):


    string = string.lower()
    list_to_search = [s.lower() for s in (list_to_search)]
    res = string in list_to_search
    print(res)

    count_calls()
    return res

string_info('Urban')
string_info('Univercity')

is_contains('CiTy', ['CitY', 'STreet'])
is_contains('GARden', ['AppLe', 'PEar', 'CherRY'])
is_contains('GARDen', ['ApPle', 'PEar', 'CherRY'])
print(calls)


