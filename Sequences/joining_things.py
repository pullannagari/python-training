flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)    # produces a new variable,
                                    # join iterates over the list for us
print(output)

print(", ".join(flowers))           # all the items must be homogeneous items to use join