# Created by : Sidney Kang
# Created on : 8 Nov. 2017
# Created for : ICS3UR
# Daily Assignment - Unit4-06
# This program checks if 2 strings are the same

def compare_strings(string_1, string_2):
    string_1 = string_1.upper()
    string_2 = string_2.upper()
    
    if string_1 == string_2:  	 
       return True
    else:
       return False


string_1 = raw_input("Enter any word: ")
string_2 = raw_input("Enter another word: ")

compare_strings(string_1, string_2)

final_answer = compare_strings(string_1, string_2)
print(final_answer)
