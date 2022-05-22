# print("Hello world")

numbers_string = 'One,Two,Three,Four,Two,Four'
total = "123,123.4"
new_price = 5

# print(numbers_string)

list_numbers = numbers_string.split(',')
# print(list_numbers)
# print(float(total.replace(',', '')) + new_price)

white_list = ("Two", "Four", "Five")

count_dict = {}
for i in list_numbers:
    if i in white_list:
        count_dict[i] = count_dict.get(i, 0) + 1

        # print(f"слово {i} находится в списке white_list")

# print(count_dict)



numbers_dict = {
    "Four" : {
        "Five" : 5,
        "Six"  : 6,
    },
    "One" : {
        "Two" : 2,
        "Three" : 3,
    }
    
}

print(numbers_dict['Four']['Six'])