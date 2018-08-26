# entering the date of birth
print("Enter the date of birth. (dd-mm-yyyy)")
date = input()
date_1 = date[0]
date_2 = date[1]
date_3 = date[3]
date_4 = date[4]
date_5 = date[6]
date_6 = date[7]
date_7 = date[8]
date_8 = date[9]
# change of data type
changed_date_1 = int(date_1)
changed_date_2 = int(date_2)
changed_date_3 = int(date_3)
changed_date_4 = int(date_4)
changed_date_5 = int(date_5)
changed_date_6 = int(date_6)
changed_date_7 = int(date_7)
changed_date_8 = int(date_8)
# summing up the digits of the date of birth
sum_date = changed_date_1 + changed_date_2 + changed_date_3 + changed_date_4 + changed_date_5 + changed_date_6 + changed_date_7 + changed_date_8
# last summation of results
str_sum_date = str(sum_date)
end_1 = str_sum_date[0]
end_2 = str_sum_date[1]
ch_end_1 = int(end_1)
ch_end_2 = int(end_2)
end_end = ch_end_1 + ch_end_2
str_end_end = str(end_end)
print("You are a numerological " + str_end_end +".")
