# Functions

# Mean Value Example


def mean(num):
    total = 0
    for i in range(num + 1):
        total += i
        print(i,total)
    return total / num

# print("Mean value",mean(6)) -- hard coded way
data = int(input("Enter the value to get Mean ")) # user input
print("Mean value",mean(data))

    
    
# Output 
# Enter the value to get Mean 5                                                                                                                            
# 0 0                                                                                                                                                      
# 1 1                                                                                                                                                      
# 2 3                                                                                                                                                      
# 3 6                                                                                                                                                      
# 4 10                                                                                                                                                     
# 5 15                                                                                                                                                     
# Mean value 3.0 
  

    
  
