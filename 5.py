with open("for_word_count.txt") as f:
    data = f.read().replace(",", " ").split(" ")
print(len(data))
