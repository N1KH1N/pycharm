# create a decorator for the given function.it will validate the phn_number either return a exception "not valid"


@valid
def change_number(phn_number):
    new_number=phn_number
    return new_number
print(change_number('+911294567890'))

