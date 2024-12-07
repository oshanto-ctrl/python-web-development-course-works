''' Lambda functions '''
# lambda functions shortens functions like list comprehension do to lists

# structure:
# lambda argument_list : expressions
# if else / loops can be write in expression.
# sum = lambda a, b : a+b
# s = sum(10, 10)
# print(f"Sum = {s}\ttype {type(s)}")

adds = lambda *args, **kwargs : (sum(args), kwargs)
print(adds(1, 14,))



