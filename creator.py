from pyscript import display

# String
name = "Paminder Singh Bhullar"
# Tuple
favorites = ("Red", "Bears", "Sloths", "Basketball")

# List
interests = ["Basketball", "Animals"]

# Add to the list
interests.append("ICT")

# Sets
animals = {"Bears", "Sloths"}
sports = {"Basketball"}

# Combine the sets
likes = animals.union(sports)

# Display information
display("Name: " + name, target="creatorInfo")
display("Favorite Color: " + favorites[0], target="creatorInfo")
display("Favorite Animals: " + favorites[1] + " and " + favorites[2], target="creatorInfo")
display("Favorite Sport: " + favorites[3], target="creatorInfo")
display("Interests: " + ", ".join(interests), target="creatorInfo")
display("Things I Like: " + ", ".join(likes), target="creatorInfo")
display("Favorite Quote: This too shall pass.", target="creatorInfo")
