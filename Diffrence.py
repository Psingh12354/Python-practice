#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
#Test Data :
#color_list_1 = set(["White", "Black", "Red"])
#color_list_2 = set(["Red", "Green"])
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(sorted(color_list_1.difference(color_list_2)))
