'''
largestNumber("I saw 3 dogs, 17 cats, and 14 cows, 20!")
'''

def largest_number(s):
    maxNo = float('-inf')
    for subS in s.split(" "):
        if subS.isdigit():
            thisNo = eval(subS)
            if (thisNo > maxNo):
                maxNo = thisNo

    if maxNo == float('-inf'):
        maxNo = None

    return maxNo

r = largest_number("I saw 3 dogs, 17 cats, and 14 cows, 20!!")
print(r)
assert(largest_number("I saw 3 dogs, 17 cats, and 14 cows, 20!!") == 17)
assert(largest_number("One person ate two hot dogs!") == None)
print("Passed")
