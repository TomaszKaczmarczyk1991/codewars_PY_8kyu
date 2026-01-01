# def set_alarm(employed, vacation):
#     if employed == False:
#         return False
#     elif employed == True:
#         if vacation == False:
#             return True
#         return False
    
def set_alarm(employed, vacation):
    return employed and not vacation