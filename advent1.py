#1 loop each line.
# find first and last nubmer in the line.
# glue them togehter 1 ,3 = 13 
#special case if it is only one number then it is like 7 -> 77
#  the take addition of each line and get a final result.


import re


txtFILE = "./inputAdvent1.txt"

def firsAndTwolastnumber(txFILE):
    sum = 0 
    with open(txtFILE, 'r') as file:
        
        for line in file:
            result = re.sub(r'\D', '',line) 
            glueDigits = "".join([result[0],result[-1]])
            sum += int(glueDigits)
    return sum
       
        
         
            
            
                
print(firsAndTwolastnumber(txtFILE))



            
                
            
                    
                
                    
                
                    
                
            
          


    
    
    