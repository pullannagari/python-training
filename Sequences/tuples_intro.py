# tuples are immutable , which is the major difference from a list
t = "a", "b", "c"
print(t)

# paranthesis are option when defining a tuple
tp = ("a", "b", "c")
print(tp)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

#metallica[0] = "Master of Puppets" you cannot change the tuple

# Because they don't have the overhead of having the methods of changing things
# it uses less memory and can be used to store large amount of data
# it can be used to protect the integrity of the data

# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)