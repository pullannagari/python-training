shopping_list = ["milk", "pasta", "eggs", "rice", "spam", "bread"]

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy {}".format(item))