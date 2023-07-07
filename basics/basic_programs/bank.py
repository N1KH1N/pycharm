fixed=5000
withdraw=float(input('Enter the Amount to be withdrawn:'))
Balance=fixed-withdraw

if withdraw<=fixed:
    print(withdraw, "Rs Has been Debited from your Account")
    print("The Balance Amount is:", Balance)

else:
    print("You Have Insufficient Balance in your Account")