def urgent(shopping_list, product):
    if product not in shopping_list:
        shopping_list.insert(0, product)
    return shopping_list

def unnecessary(shopping_list, product):
    if product in shopping_list:
        shopping_list.remove(product)
    return shopping_list

def correct(shopping_list, product, new_product):
    if product in shopping_list:
        shopping_list[shopping_list.index(product)] = new_product
    return shopping_list

def rearrange(shopping_list, product):
    if product in shopping_list:
        shopping_list.remove(product)
        shopping_list.append(product)
    return shopping_list



grocery_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        print(", ".join(grocery_list))
        break

    current_command = command.split()
    action = current_command[0]
    item = current_command[1]

    if action == "Urgent":
        grocery_list = urgent(grocery_list, item)

    elif action == "Unnecessary":
        grocery_list = unnecessary(grocery_list, item)

    elif action == "Correct":
        new_item = current_command[2]
        grocery_list = correct(grocery_list, item, new_item)

    elif action == "Rearrange":
        grocery_list = rearrange(grocery_list, item)

