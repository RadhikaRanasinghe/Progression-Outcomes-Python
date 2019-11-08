#Declaring variables
passed_credits = 0
deferred_credits = 0
failed_credits = 0
total_credits = 0
values_approved = False

#Unicode characters for creation of the table
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"

print(top_left_corner+horizontal*100+top_right_corner)
print(vertical+"             P R O G R E S S I O N   O U T C O M E S  :  S T U D E N T   V E R S I O N              "+vertical)
print(bottom_left_corner+horizontal*100+bottom_right_corner)
print()


def user_inputs():#Functions to take inputs and count the number of students' credits are entered
    global student_count,passed_credits,deferred_credits,failed_credits,values_approved
    #All three credits category inputs are taken from the user
    passed_credits = int(input("Enter the number of credits student has passed (Including condoned passes)\t:"))
    deferred_credits = int(input("Enter the number of credits student has defered\t\t\t\t\t:"))
    failed_credits = int(input("Enter the number of credits student has failed\t\t\t\t\t:"))
    print()
    print()
    total_credits = (passed_credits + deferred_credits + failed_credits)
    if total_credits ==120: #Checking if the total of the scores entered are equal to 120 if not user has to input again
        if passed_credits % 20 == 0 and deferred_credits % 20 == 0 and failed_credits % 20 == 0:
            #Checking if the values entered are divisible by 20 if not user has to input again
            values_approved = True #If both of the conditions are true, values are approved for processing
            student_count += 1
        else: 
            print("Range Error! Please enter correct credits values.")#Divisible by 20 condition has become false
            print()
            user_inputs()
    else:
        print("Total Error! Please enter correct credits values which sums upto 120.")#Total of 120 condition has become false
        print()
        user_inputs()
    return student_count,passed_credits,deferred_credits,failed_credits,values_approved
    
def progress_outcome():
    print(top_left_corner+horizontal*74+top_right_corner)
    if passed_credits == 120:
        print(vertical+"\t\tProgression outcome:\tP R O G R E S S\t\t\t  ",vertical)
    elif passed_credits == 100:
        print(vertical+"\t\tProgression outcome:\tProgress- Module trailer\t  ",vertical)
    elif passed_credits <= 80 and failed_credits < 80:
        print(vertical+"\tProgression outcome:\tDo not Progress- Module Retriever\t  ",vertical)
    elif failed_credits >= 80:
        print(vertical+"\t\t\tProgression outcome: E x c l u d e\t\t  ",vertical)
    print(bottom_left_corner+horizontal*74+bottom_right_corner)

#Main Program calling the user defined fucntions 
try: 
    user_inputs()
    if values_approved == True:
       progress_outcome()    
except: 
    print("Integers Required!")