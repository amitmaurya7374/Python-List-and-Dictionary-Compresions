sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
text = sentence.split()
result = {word: len(word) for word in text}

print(result)



