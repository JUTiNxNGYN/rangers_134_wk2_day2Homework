# Fizz Buzz 
# Given a random number as an input to a function, 
# return "FIZZ" if the number is even and 
# "BUZZ" if the number is odd

def random_number(num):
    if num % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"
    
print(random_number(5))