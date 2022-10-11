# List, Tuple, Dictionaries and Sets are the Four Horsemen of Data Structure in Python 

# List: Unordered, mutable, []
songs = ['Heathens', 'Chlorine', 'Ride', 'Saturday']

print(songs[2]) # Accessing
print(songs[1:3]) #Slicing

songs.append("Jumpsuit") # Add an item at the end of the list
print(songs)

songs.insert(1, "Car Radio") # Add an item at the index of our choice
print(songs)

songs.extend(["Stressed out", "My blood"]) # Add multiple items
print(songs)

del songs[1] # def fn deletes items based on index
print(songs)

songs.pop(3) # .pop() also deleted based on index
print(songs)

songs.remove('Ride')
print(songs)

songs[2] = "Level of concern" # Replace an item
print(songs)

songs = ["Heavydirtysoul" if i == 'Chlorine' else i for i in songs] # List comprehension to replace values
print(songs)

songs.sort() # Sort items in the list
print(songs)

songs.clear() # Removes all element from the list
print(songs)


print("-----------------------------------------------")

# Tuples: Ordered, immutable, ()

songID = (1234, 3456, 4567, 5678, 7890)
print(songID[1]) # Accessing
print(songID[1: 4]) #Slicing
print(sorted(songID)) # Sorting
song1, song2, song3 = (1, 2, 3) # Assignment
print(song1, song2, song3)
songID_1 = (1234, 3456, 4567, 5678, 7890)
songID_2 = songID_1 + (3242, 5253, 6363)
print(songID_2) # concatenation


print("------------------------------------------------")

# Dictionaries: Unordered, mutable, key:value

employee = {  
        "name":       "Rick",   
        "salary":      56000,   
        "married":    True  
    }  

print(employee)
print(employee['name']) #Accessing
print(employee.keys()) # Viewing keys
print(employee.values()) # Viewing values

employee['role'] = "Developer" # Add element
print(employee)

del employee['married'] #def fn
print(employee)

employee.pop('salary') #.pop() fn
print(employee)

employee.clear() # clearing

print("------------------------------------------------")

# Sets: Unordered, mutable, no repleated values, {}

genres = {"Rock", "Folk", "Hip Hop", "Pop Sauce"}
print(genres)

genres.add("Electronic") # Add items
print(genres)

genres.update(['Blues', 'Punk']) # Add multiple items
print(genres)

genres.remove('Punk') # Removes an element
print(genres) 
