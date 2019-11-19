

IDs         = []  #Contains the individual unique Id's of the employees
length      = 0   #Stores the length of each id


for _ in range(int(raw_input())):   #Runs a loop to take the said number of id's based on the user input
    IDs.append(raw_input().split()) #Appends each id as a sub array to the IDs array(database for employee IDs)

for i in IDs :                      #Loops through  sub arrays in IDs
    for j in i:                     #Loops through each employee ID
        
       length = len(j)              #Calculates the length of the employee ID
        
       
            
        unkown_char = 0             #Variable check if there's any non alphanumeric character
        repeatition = 0             #Variable to check for repitition
        uppercase   = []            #Contains all alphabet characters of the ID
        digits      = []            #Contains all numbers of the ID
        
        for k in j:                 #Loops through the individual characters of each employee ID
            
            
            if(k.isupper() or k.islower()):    #Checks for a letter as a character
                if(k not in uppercase):         #Checks for repitition
                    uppercase.append(k)

                else:
                    repeatition = 1;
               
            
            elif(k.isdigit()):                  #Checks for number as a charcter
                if(k not in digits):            #Checks for repitition
                    digits.append(k)
                else:
                    repeatition = 1;
                

            else:                               #Checks for non alphanumeric character
                unkown_char = 1;


         #Based on all the checks, this statement Validates the ID as being valid or invalid based on the requirments       
        if((repeatition == 0) and (unkown_char == 0) and (length == 10) and (len(digits) >= 3) and (len(uppercase) >= 2) ):     
            print("Valid")

        else:
            print("Invalid")


