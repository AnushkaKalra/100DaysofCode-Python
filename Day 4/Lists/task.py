states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Accessing items in list
print(f"The first state in the list is: {states_of_america[0]}") #positive indexing
print(f"The last state in the list is: {states_of_america[-1]}") #negative indexing

#Modifying items in list
states_of_america[1] = "Georgia"
print(f"The second state in the list is: {states_of_america[1]}") #Modified Pennsylvania to Georgia

#Adding items in list
states_of_america.append("Pennsylvania")
print(f"The States of America:\n{states_of_america}")

states_of_america.extend(["AngelaLand, ABCLand"])
print(f"The States of America:\n{states_of_america}")
