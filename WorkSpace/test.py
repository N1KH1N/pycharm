# ads="THIS is a Python PROGRAMMING challenge"

def case_count(ads):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    blank = " "
    upper_count = 0
    lower_count = 0
    blank_count = 0
    flag=0

    for i in ads:
        # if i not in upper and i not in lower and i not in blank:
        #     return "invalid"
        if i in upper:
            upper_count += 1
            flag+=1
        elif i in lower:
            lower_count += 1
            flag+=1
        elif i in blank:
            blank_count += 1
            flag+=1


    count = dict(lower_case=lower_count, upper_case=upper_count, white_space=blank_count)
    if ads == "":
        return {}

    elif flag==0:
        return "invalid"

    else:
        return(count)

ads=input("Enter the Sentence:- ")
print(case_count(ads))