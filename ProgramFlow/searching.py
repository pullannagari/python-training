shopping_list = ["milk", "pasta", "eggs", "rice", "spam", "bread"]

item_to_find = "spam"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == "spam":
        found_at = index
        break
if found_at is not None:
    print("Item found at {}".format(found_at))

#below code represents the same actions
if item_to_find in shopping_list:
    print("Item found at {}".format(shopping_list.index(item_to_find)))
