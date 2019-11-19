

IDs         = []  #Contains the individual unique Id's of the employees
length      = 0   #Stores the length of each id


for _ in range(int(raw_input())):   #Runs a loop to take the said number of id's based on the user input
    IDs.append(raw_input().split()) #Appends each id as a sub array to the IDs array(database for employee IDs)

for i in IDs :          #Loops through each sub array in IDs
    for j in i:         #Loops through 
        
        if(len(j)==10):
            length =10
        
       
            
        unkown_char = 0
        repeatition = 0
        uppercase   = []
        digits      = []
        for k in j:
            
            if(k.isupper() or k.islower()):
                if(k not in uppercase):
                    uppercase.append(k)

                else:
                    repeatition = 1;
               
            
            elif(k.isdigit()):
                if(k not in digits):
                    digits.append(k)
                else:
                    repeatition = 1;
                

            else:
                unkown_char = 1;


        if((repeatition == 0) and (unkown_char == 0) and (length == 10) and (len(digits) >= 3) and (len(uppercase) >= 2) ):
            print("Valid")

        else:
            print("Invalid")


