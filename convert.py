from fontTools.ttLib import TTFont

# Insert the path of the file you want to convert
font = TTFont("path")

# Change the extension name
font.flavor = "extension"

# Save the file with its respective path
font.save("path")

# And run the file in the environment
# * "py convert.py"
