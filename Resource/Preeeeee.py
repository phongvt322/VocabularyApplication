# Test
# N = 1000
# with open("anhviet109K.txt") as myfile:
#     head = [next(myfile) for x in range(N)]
#     f = open("anhviet109K_test.txt", "w")
#     f.write(''.join(head))
#     f.close()


# with open("Oxford 5000.txt") as myfile:
#     with open("anhviet109K.txt") as myfile:
#         data="".join(line.rstrip() for line in myfile)

# Test #2
# list = ['a','b','c','d']
# print("@"" + list)

# abandon
import pickle
with open("anhviet109K.txt") as dict_file:
    with open("Oxford 5000.txt") as fiveTh_file:
        # words_5000 = [next(fiveTh_file) for x in range(N)]
        pattern_5000W = ["@" + line + " /" for line in fiveTh_file.read().splitlines()]
        index_dict = {}
        new_word_flag = False
        for index, line in enumerate(dict_file):
            if "@" in line and new_word_flag == True:
                index_dict[new_word].append(index - 2)
                new_word_flag = False
            if any(words in line for words in pattern_5000W):
                word = line[1:line.find(" /")]
                index_dict[word] = [index]
                new_word_flag = True
                new_word = word
                print(str(index) + word , flush = True)
                pattern_5000W.remove("@" + word + " /")
        with open('index_dict.pkl', 'wb') as f:
            pickle.dump(index_dict, f, pickle.HIGHEST_PROTOCOL)


with open("Resource/anhviet109K.txt") as dict_file:
    word_index = dict_file.readlines()[100000]
    print(word_index)
