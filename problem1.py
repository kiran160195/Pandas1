import pandas as pd  
    
lst = [['FirstName1', 'LastName1'], 
    ['FirstName2', 'LastName2'], 


df = pd.DataFrame(lst, columns =['First_Name', 'Last_Name']) 
print(df )