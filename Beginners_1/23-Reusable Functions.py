def emoji_converter(message):
    words = message.split(' ')  # convierto el input de message en una lista
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
        return output
message = input(">")
print(emoji_converter(message))