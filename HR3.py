def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        leap = True
    elif(year % 4 == 0 and year % 100 == 0):
        leap = False
    elif (year % 4 == 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

#  if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True