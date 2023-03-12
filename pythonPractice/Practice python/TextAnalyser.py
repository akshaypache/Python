def aadesh(text):
    def count_char(text, char):
        count = 0
        for c in text:
            if c == char:
                count +=1
        return count
    text = text.lower()
    for char in "abcdefghijklmnopqrstuvwxyz":
        percent = 100 * count_char(text, char)/len(text)
        print(f"{char} -> {round(percent,2)}%")


aadesh("aadesh")