ascii = 33
for i in range(32):
    coloum1 = f"'{chr(ascii)}'    =>    {ascii}"
    coloum2 = f"'{chr(ascii+32)}'    =>    {ascii+32}"
    coloum3 = f"'{chr(ascii+64)}'    =>    {ascii+64}"
    print(f"|   {coloum1}   |   {coloum2}   |   {coloum3}\t|")
    ascii = ascii+1
