states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

# Length of List
print(f"The number of states in the list are: {len(states_of_america)}.")

# Checking Index Error
#print(states_of_america[4]) # No Index Error
#print(states_of_america[55]) # Index Error

# Nested Lists
cities_of_america = ["New York, Los Angeles, Houston, Chicago, San Francisco, Las Vegas, Seattle, Boston"]

states_and_cities = [states_of_america, cities_of_america]
print(states_and_cities)
