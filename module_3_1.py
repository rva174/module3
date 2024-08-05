
calls = 0
def count_calls():
    calls = calls + 1


    return calls


def string_info(string):

#    global calls
 #   count_calls()
 #   calls = calls + 1

    string_info = (len(string), string.upper(), string.lower())
    print(string_info)

    return string_info

def is_contains(string, list_to_search):

    string = string.lower()
    list_to_search = [s.lower() for s in (list_to_search)]
    print(string, list_to_search)

    res = string in list_to_search
    print(res)
 #   calls == calls + 1
  #
#    calls
#    count_calls()

 #   global(calls)
  #  calls += 1

    return res

string_info('Urban')
string_info('Univercity')

is_contains('CiTy', ['CitY', 'STreet'])
is_contains('GARden', ['AppLe', 'PEar', 'CherRY'])
print(calls)


