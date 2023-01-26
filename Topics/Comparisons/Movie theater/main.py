number_of_halls = int(input())
capacity = int(input())
number_of_vievers = int(input())

if(number_of_halls * capacity >= number_of_vievers):
    print(True)
else:
    print(False)