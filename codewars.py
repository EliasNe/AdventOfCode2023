#mean()
import math

import statistics
lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']

def countmean(lst):
    numberList =[]
    stringList = ""
    finalList = []
    
    for char in lst:
        # print(char)
        if char.isdigit():
            charToint = int(char)
            numberList.append(charToint) 
        else:
            stringList += char     
    resultMean = statistics.mean(numberList)
    
    finalList.append(resultMean)
    finalList.append(stringList)
    
    return finalList

     
def countmean2(lst):
    numberList =[]
    stringList = ""
    finalList = []
    
    numberList = [int(char) for char in lst if char.isdigit() ]
    stringList = [ stringlist +=char for char in lst if not char.isdigit() ]
    
    resultMean = statistics.mean(numberList)
    
    finalList.append(resultMean)
    finalList.append(stringList)
    
    return finalList   
            
        

print(countmean2(lst))