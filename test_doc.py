import random
test_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
# dict_keys = test_dict.keys()
# print(dict_keys)
# random.shuffle(dict_keys)
# for key in dict_keys:
#     print(key)
#     print(test_dict[key])


keys = list(test_dict.keys())
print(keys)
random.shuffle(keys)
for key in keys:
    print(key, test_dict[key])