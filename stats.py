"""
1. Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
Each dictionary should have a single key-value pair, where the key is the character and the value is the count.
Sort from greatest to least by the count.
The .sort() method will be helpful here (see the hint).
2. Import and call the function in main.py, and capture the result.
3. Print the report to the console as shown above. If the character is not an alphabetical character 
(using the .isalpha() method), just skip it
"""
def get_num_words(any_string):
    return len(any_string.split())

def get_num_chars(any_string):
    char_counts = {}
    for char in any_string:
        if char.lower() in char_counts and char.isalpha() == True:
            char_counts[char.lower()] += 1
        elif not char.lower() in char_counts and char.isalpha() == True:
            char_counts[char.lower()] = 1
        else: 
            pass
    return char_counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return list(dict.values())

def create_sorted_list_of_dicts(dict):
    dict_list = []
    for char in dict:
        single_dict = {}
        count = dict[char]
        single_dict[char] = count
        dict_list.append(single_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list



"""
vehicles = [
    {"name": "car", "num": 7},
    {"name": "plane", "num": 10},
    {"name": "boat", "num": 2}
]
vehicles.sort(reverse=True, key=sort_on)
print(vehicles)
"""
# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]
"""
planet_distances = {
    "Mercury": 57.91,
    "Venus": 108.2,
    "Earth": 149.6
}

for planet in planet_distances:
    distance = planet_distances[planet]
    print(f"Planet: {planet}, Distance: {distance} million km")
"""
# Planet: Mercury, Distance: 57.91 million km
# Planet: Venus, Distance: 108.2 million km
# Planet: Earth, Distance: 149.6 million km