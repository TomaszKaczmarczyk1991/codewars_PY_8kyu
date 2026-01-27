# def is_loch_ness_monster(string):
#     if ('tree fiddy' in string or
#         'three fifty' in string or
#         '3.50' in string):
#         return True
#     return False


def is_loch_ness_monster(string):
    return any(x in string for x in ['tree fiddy', 'three fifty', '3.50'])
