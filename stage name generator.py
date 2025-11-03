import random
#Stage Name Generator: Create two lists of words- fill the first one with 10 adjectives
#(i.e. "'lil", "stinky", "green", etc). Fill the second one with nouns (i.e. "Potato", "Pete", "Sock").
#Randomly pick a word from each and print it to the screen. Once this works, put the whole thing in a loop that runs until a user types 'q'.



adj = ["'lil", "stinky", "green","big", "happy", "old", "new", "beautiful", "cold", "hot"]

noun = ["Potato", "Pete", "Sock", "cat" , "table" , "water" , "car", "love" , "anger" , "fire"]

x = random.randint(0, 9)
 
y = random.randint(0, 9)

print(x, y)

print(adj[x], noun[y])
