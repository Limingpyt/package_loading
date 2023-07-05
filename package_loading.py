
items_amount = int(input("Enter number of items to be sent:"))

package_weight = 0
sent_packages = 0
total_sent_weight = 0

empty_space = 0
last_package_empty = 0
current_empty_space = 0

for item in range(items_amount):
    item_weight = int(input(f"Enter the weight of the item number {item + 1}: "))

    if item_weight < 1 or item_weight > 10:
        print("Item weight must be between 1 and 10 kg")
        break


    package_weight += item_weight

    if package_weight > 20:
        sent_packages += 1
        total_sent_weight += package_weight - item_weight
        package_weight = item_weight
        empty_space = 20 - package_weight #?
        
    elif package_weight == 20:
        sent_packages += 1
        total_sent_weight += package_weight
        package_weight = 0
        empty_space = 20 - package_weight #?

    if item == items_amount - 1:
        sent_packages += 1
        total_sent_weight += package_weight
        empty_space = 20 - package_weight #?
        

    if empty_space == 20 - package_weight: #?
        last_package_empty = sent_packages
        

    

    if current_empty_space > last_package_empty:
        current_empty_space = last_package_empty #?
        

total_empty_space = sent_packages *20 - total_sent_weight
        
print(f"Sent packages:{sent_packages}")
print(f"Sent weight:{total_sent_weight} kg")        
print(f"Empty space:{total_empty_space} kg")
print(f"Most empty package: {last_package_empty}")
