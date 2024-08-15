def calculate_structure_sum(data_structure):

    if isinstance(data_structure,int):
        return data_structure
    elif isinstance(data_structure,str):
        return len(data_structure)
    elif (isinstance(data_structure,list) or
           isinstance(data_structure,tuple) or
           isinstance(data_structure,set) ):
        sum = 0
        for item in data_structure:
            sum += calculate_structure_sum(item)
        return sum

    elif isinstance(data_structure,dict):
        sum = 0
        for key,value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
        return sum
    else:
        print('unsupperted type',type(data_structure),data_structure)

data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print("Сумма всех чисел и длин всех строк: ", result)