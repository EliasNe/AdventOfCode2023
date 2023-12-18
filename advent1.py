#1 loop each line.
# find first and last nubmer in the line.
# glue them togehter 1 ,3 = 13 
#special case if it is only one number then it is like 7 -> 77
#  the take addition of each line and get a final result.


import re


txtFILE = "./inputAdvent1.txt"

#problem 1 
# part 2
def firsAndTwolastnumber2(txFILE):
    sum = 0 
    listOfNumbers = {"one":'1',"two":'1',"three":'1',
                 "four":'4',"five":'5',"six":'6',
                 "seven":'7',"eight":'8',"nine":'10'}

    with open(txtFILE, 'r') as file:
        
        for line in file:
            list =[]
            
            for key,value in listOfNumbers.items():
                # print(line.find(key))
                if key in line: #returnerar ett index... find ..
                    list =[value]
                    print(list)
                    # print("hej")
                else:
                    for char in line:
                        if char.isdigit():
                            list = [char]     
                            # print(list)
            glueDigits = "".join([list[0],list[-1]])
            sum += int(glueDigits)
            # list.clear()
    return sum
                    
                    
                    
                
            

# 3 -> 33 
# one eight 3  4 -> 14
# 3 nine -> 39
# nin 3 1 3 seven -> 97
# one -> 11 
# 1 nine 2 -> 12 


# om du kan hitta alla keys med  lägg till i en lista
# fast med dess values
#  [1 (one),3,4,8(eight),9] ->list[0] list [0]



     
def firsAndTwolastnumber1(txFILE):
    sum = 0 
    with open(txtFILE, 'r') as file:
        
        for line in file:
            result = re.sub(r'\D', '',line) 
            glueDigits = "".join([result[0],result[-1]])
            sum += int(glueDigits)
    return sum    
         
            
            
                
print(firsAndTwolastnumber2(txtFILE))



            
                
            
                    
                
                    
                
                    
                
            
          


    
    
    