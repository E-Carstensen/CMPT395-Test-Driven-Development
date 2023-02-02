

def fizzbuzz(i):
    
    if not isinstance(i, int):
        return False

    output = ""

    if i % 3 == 0:
        output = output + "Fizz"

    if i % 5 == 0:
        output = output + "Buzz"

    if len(output) == 0:
        output = output + str(i)

    return output


