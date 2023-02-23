from prettytable import PrettyTable

vowels = ["A","a","i","ee","u","oo","e","ai","o","au","am","an"]

table = PrettyTable( vowels )

letters = ["k","kh","g","gh","ch","chh",
           "j","jh","t","th","d","d","n",
           "t","th","d","dh","n","p","ph",
           "b","bh","m","y","r","l","w",
           "sh","sh","s","h","ksh","gy"]

for char in letters:
    list = []
    for i in vowels:
        list.append( char + i )
    table.add_row( list )

barakhadi = str( table ).upper() 

print( barakhadi )