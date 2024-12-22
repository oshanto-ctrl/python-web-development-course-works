'''
Error Handling Methods.
1. try
2. except
3. else
4. finally
5. raise
'''

### Type of errors

## 1. Syntax Error
# print("Hikaru Nakamura)
      
## 2. NameError
# print(a)

## 3. TypeError
# print("Hikka" - 3)

## 4. IndentationError
# if 1 < 2:
# print("HHH")

## 5. keyError
# d = {1:"a", 2:"b", 3:"c"}
# print(d[3])

## 6. zeroDivisionError
# print(400/0)
try:
    x = 10/0
    print(x)
except Exception as e:
    print(type(e))
    print(e) # e is class 'ZeroDivisionError'
    print(type(str(e)))
    print(str(e)) # e is string 'division by zero'


# raise example
# Exception inside message will be shown to user.
def test(a):
    if a < 0:
        raise Exception("Number should be positive.")
    else:
        a += 10.
        print(a)
# call test
test(-5)
# test(-10)