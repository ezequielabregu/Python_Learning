message = input(">")
words = message.split(' ')                  # convierto el input de message en una lista
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)