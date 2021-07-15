arr = list([1, 2])

def createarr(arr):
 arr = [5,6,7]
 return arr

def appendarr(arr):
 arr.append(3)
 return arr

# creating new list leads to change in object reference
print(createarr(arr))
print(arr)
print(appendarr(arr))
print(arr)

