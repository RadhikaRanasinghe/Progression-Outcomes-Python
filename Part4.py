#Initialization of variables
pass_counter = [120,100,100,80,60,40,20,20,20,0]
defer_counter = [0,20,0,20,40,40,40,20,0,0]
fail_counter = [0,0,20,20,20,40,60,80,100,120]
student_count = len(pass_counter)
progress_count = 0
trailing_count = 0
retriver_count = 0
excluded_count = 0
rs_progress_count = 0
rs_trailing_count = 0
rs_retriver_count = 0
rs_excluded_count = 0


#Unicode characters for creation of the table
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"
right_junction = "\u2563"
left_junction = "\u2560"

print(top_left_corner+horizontal*100+top_right_corner)
print(vertical+"    P R O G R E S S I O N   O U T C O M E S  :  S T A F F  V E R S I O N   ( E X T E N S I O N )    "+vertical)
print(bottom_left_corner+horizontal*100+bottom_right_corner)
print()

def progress_outcome():# All of the students' progress outcome predictions are printed on the console
    global progress_count,trailing_count,retriver_count,excluded_count,rs_progress_count,rs_trailing_count,rs_retriver_count,rs_excluded_count
    for i in range(0,len(pass_counter)):#No of student records are taken from the length of a list
        if pass_counter[i] == 120:
            print("Progression outcome of student",[i+1],": Progress")
            print()
            progress_count +=1
            rs_progress_count +=1
        elif pass_counter[i] == 100:
            print("Progression outcome of student",[i+1],": Progress- Module trailer")
            print()
            trailing_count += 1
            rs_trailing_count += 1
        elif pass_counter[i] <= 80 and fail_counter[i]< 80:
            print("Progression outcome of student",[i+1],": Do not Progress- Module Retriever")
            print()
            retriver_count += 1
            rs_retriver_count += 1
        elif fail_counter[i] <= 120:
            print("Progression outcome of student",[i+1],": Exclude")
            print()
            excluded_count +=1
            rs_excluded_count +=1
    return progress_count,trailing_count,retriver_count,excluded_count,rs_progress_count,rs_trailing_count,rs_retriver_count,rs_excluded_count
    
def resetVar(): #Resetting variables for only when vertical histogram is asked before the horizontal histogram
    global progress_count,trailing_count,retriver_count,excluded_count,rs_progress_count,rs_trailing_count,rs_retriver_count,rs_excluded_count
    progress_count = rs_progress_count
    trailing_count = rs_trailing_count
    retriver_count = rs_retriver_count
    excluded_count = rs_excluded_count
    return progress_count,trailing_count,retriver_count,excluded_count

def menu_histogram():#Asking user input only for the choice of horizontal, vertical, or to quit
    global progress_count,trailing_count,retriver_count,excluded_count,student_count
    histogram = str(input("Enter 'H' for a horizontal histogram, 'V' for vertical histogram or any other key to Quit\t:"))
    if histogram == "H" or histogram == "h":
        horizontal_histogram()
        print()
        another_histogram = str(input("Enter 'V' for another vertical histogram or any other key to Quit\t:"))
        print()
        if another_histogram == 'v' or another_histogram == 'V':
            vertical_histogram()
        else: 
            print("Quiting.......")
            pass
    elif histogram == "V" or histogram == "v":
        vertical_histogram()
        print()
        another_histogram = str(input("Enter 'H' for another horizontal histogram or any other key to Quit\t:"))
        print()
        if another_histogram == 'h' or another_histogram == 'H':
            horizontal_histogram()
        else:
            print("Quiting.......")
            pass
    else:
        print("Quiting.......")
        pass

def horizontal_histogram():#Printing the horizontal histogram with a border
    global progress_count,trailing_count,retriver_count,excluded_count,student_count
    p_count = 76-progress_count
    t_count = 76-trailing_count
    r_count = 76-retriver_count
    e_count = 76-excluded_count
    print()
    print()
    print(top_left_corner+horizontal*100+top_right_corner)
    print(vertical+"                               H O R I Z O N T A L    H I S T O G R A M                             "+vertical)
    print(left_junction+horizontal*100+right_junction)
    print(vertical+f'{vertical:>101}')
    print(vertical+"Progress    (",f'{progress_count:02}',")    :","*"*progress_count+" "*(p_count)+vertical)
    print(vertical+f'{vertical:>101}')
    print(vertical+"Trailing    (",f'{trailing_count:02}',")    :","*"*trailing_count+" "*(t_count)+vertical)
    print(vertical+f'{vertical:>101}')
    print(vertical+"Retriever   (",f'{retriver_count:02}',")    :","*"*retriver_count+" "*(r_count)+vertical)
    print(vertical+f'{vertical:>101}')
    print(vertical+"Excluded    (",f'{excluded_count:02}',")    :","*"*excluded_count+" "*(e_count)+vertical)
    print(vertical+f'{vertical:>101}')
    print(left_junction+horizontal*100+right_junction)
    print(vertical+"Total number of students:   (",f'{student_count:02}',")"+f'{vertical:>67}')
    print(bottom_left_corner+horizontal*100+bottom_right_corner)

def vertical_histogram():#Printing the vertical histogram with a border
    global progress_count,trailing_count,retriver_count,excluded_count,student_count
    print(top_left_corner+horizontal*100+top_right_corner)
    print(vertical+"                                V E R T I C A L   H I S T O G R A M                                 "+vertical)
    print(left_junction+horizontal*100+right_junction)
    print(vertical+f'{vertical:>101}')
    print(vertical+"        Progress        ","        Trailing        ","        Retriever       ","        Excluded        ",vertical)
    print(vertical+" "*100+vertical)
    while progress_count!=0 or trailing_count !=0 or retriver_count !=0 or excluded_count !=0:
        if progress_count > 0:
            print(vertical+"           *    ",end="\t")
            progress_count -=1
        else:
            print(vertical+"                ",end="\t")
        if trailing_count > 0:
            print("             *    ",end="\t")
            trailing_count -=1
        else:
            print("                 ",end="\t")
        if retriver_count > 0:
            print("\t       *        ",end="\t")
            retriver_count -=1
        else:
            print("\t                ",end="\t")
        if excluded_count > 0:
            print("       *            ",vertical,end="\n")
            excluded_count -=1
        else:
            print("                    ",vertical,end="\n")
    resetVar()
    print(vertical+" "*100+vertical)
    print(left_junction+horizontal*100+right_junction)
    print(vertical+"Total number of outcomes:",f'{student_count:02}',f'{vertical:>72}')
    print(bottom_left_corner+horizontal*100+bottom_right_corner)

#Main Program
progress_outcome()
menu_histogram()
    
