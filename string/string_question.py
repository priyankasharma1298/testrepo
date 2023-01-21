# string ='zewmyde'    o/p = 5
# string ='moosmyf'    o/p = 3
# in one operation you can remove a character from the begining or the end of string
# the operation can be repeated multiple times
# FIND MINNIMUM NUMBER OF OPERATIONS NEEDED SO THAT THERE IS A CHARACTER IN THE STRING
# WHICH HAS A FREQUENCY AT LEAST HALF OF THE LENGTH OF THE STRING 

def min_operations(list_str , len_of_list_str): 
    j=0 
    dic_count={}
    opreation_count=0

    while j < len_of_list_str :
        list_str.pop() 
        if len(list_str) == 0:
            return 0
        else:    
            opreation_count+=1
            half_lenght = len(list_str)//2

            for i in list_str:
                if i in dic_count:
                    dic_count[i]+=1
                else:
                    dic_count[i]=1
            
                for value in dic_count:
                    if half_lenght == dic_count[value]:
                        return opreation_count+1
         

string ='zewmyde'
list_str = list(string)
len_of_list_str = len(list_str)
print( min_operations( list_str , len_of_list_str ) ) 


def min_operations_2(str): 
    half_length = str(len)//2
    dict_count = {}
    for ch in str:
        if ch in dict_count:
            dict_count[ch] +=1
        else :
            dict_count[ch]=1
     
    max_count_from_dict = get_max_from_dict(dict_count)
    if max_count_from_dict>=half_length:
        return 0

     

        
