from collections import defaultdict

"""
HASH TABLE EXPLANATION:

A hashmap (also referred as a dictionary in Python) is a DS that stores information (values) and pairs them with unique identifier (keys).
HashMaps are beneficial because custom keys are easier for SE to work with. In addition, HashMaps allow for search in 0(1), whereas arrays/linked lists are 0(n). So searching a value with HM is FASTER!

Any key in a HM must be an IMMUTABLE DATA TYPE. 
If you try to assign a mutable type of data as a key, such an an array, an error will pop-up, the solution to this is to convert the array into a tuple()

There are three methods to retrieve data:
- hashmap.keys() = Returns all the "keys" of the dictionary on the form of a list
- hashmap.values() = Returns all the "values" of the dictionary on the form of a list
- hashmap.items() =  Returns a list of all of the key-values as a tuple
"""


# When we are adding "values" to the key of "GPA". However, before inserting values, the key must be initiated.
# Using DefaultDict(), makes the process easier because it automatically initiates all keys.

university_gpa = defaultdict(list)
gpa_1 = ["20%", "57%", "90%"]
gpa_2 = ["20%", "57%", "90%"]
gpa_3 = ["20%", "57%", "90%"]

university_gpa["Josh"] += gpa_1
university_gpa["Miguel"] += gpa_2
university_gpa["Juan"] += gpa_3
print(university_gpa.items())
print(university_gpa.values())
print(university_gpa.keys())