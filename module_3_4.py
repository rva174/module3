def single_root_words(root_words, *other_words):  #*args

    same_words = []

    for item in other_words:
        if (root_words.lower() in (item.lower()) or (item.lower()) in root_words.lower()):
            same_words.append(item)

    print('result_1:', same_words)


result1 = single_root_words('rich','richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
