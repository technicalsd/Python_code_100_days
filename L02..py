states_of_us = ["Delaware","Pennsylvania","New jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina"]
print(states_of_us[2])
states_of_us.append("Saurabhland")
print(states_of_us)
states_of_us.extend(["Akashland","Arunland","Arunaland"])
print(states_of_us)
states_of_us.reverse()
print(states_of_us)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Above is string spliting method
