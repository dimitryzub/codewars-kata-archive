'''
CTRL + F will be enough to find a challenge
'''

# Holy cats

def holycats(cats):
    # return [item for item in cats if item == '^(~_~)^' or item == '*(^_^)*' or item == '"(^_^)"']
# or
    # new_list = []
    # for item in cats:
    #     if item == '^(~_~)^' or item == '*(^_^)*' or item == '"(^_^)"':
    #         new_list.append(item)
    # return new_list
# or
    return [cat for cat in cats if not cat in ["wicked", "normal"]]

# print(holycats(['wicked', 'wicked', '"(^_^)"', '^(~_~)^', 'normal', 'wicked', '*(^_^)*']))

# Create Phone Number
def create_phone_number(n):
    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])


    return f'({str1}) {str2}-{str3}'

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
