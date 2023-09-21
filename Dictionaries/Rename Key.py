fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
key = input()
new_key = input() 
fruits_details = list(fruits.items())
fruits_details_copy= fruits_details.copy()


fruit_count = len(fruits_details)
for i in range(fruit_count):
    if fruits_details[i][0] == key:
        updated_tuple = (new_key, fruits_details[i][1])
        fruits_details_copy[i] = updated_tuple 
print(fruits_details_copy)
