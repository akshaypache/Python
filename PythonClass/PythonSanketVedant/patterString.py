pattern = [
    ["           ","           ","           ","           ","           ","           ","           "],
    ["   ###     ","  ## ##    "," ##   ##   ","##     ##  ","#########  ","##     ##  ","##     ##  "],
    ["########   ","##     ##  ","##     ##  ","########   ","##     ##  ","##     ##  ","########   "],
    [" ######    ","##    ##   ","##         ","##         ","##         ","##    ##   "," ######    "], 
    ["########   ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","########   "],
    ["########   ","##         ","##         ","######     ","##         ","##         ","########   "],
    ["########   ","##         ","##         ","######     ","##         ","##         ","##         "],
    [" ######    ","##    ##   ","##         ","##   ####  ","##    ##   ","##    ##   "," ######    "], 
    ["##     ##  ","##     ##  ","##     ##  ","#########  ","##     ##  ","##     ##  ","##     ##  "],
    ["####       "," ##        "," ##        "," ##        "," ##        "," ##        ","####       "],
    ["      ##   ","      ##   ","      ##   ","      ##   ","##    ##   ","##    ##   "," ######    "], 
    ["##    ##   ","##   ##    ","##  ##     ","#####      ","##  ##     ","##   ##    ","##    ##   "],
    ["##         ","##         ","##         ","##         ","##         ","##         ","########   "],
    ["##     ##  ","###   ###  ","#### ####  ","## ### ##  ","##     ##  ","##     ##  ","##     ##  "],
    ["##    ##   ","###   ##   ","####  ##   ","## ## ##   ","##  ####   ","##   ###   ","##    ##   "],
    [" #######   ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  "," #######   "], 
    ["########   ","##     ##  ","##     ##  ","########   ","##         ","##         ","##         "],
    [" #######   ","##     ##  ","##     ##  ","##     ##  ","##  ## ##  ","##    ##   "," ##### ##  "], 
    ["########   ","##     ##  ","##     ##  ","########   ","##   ##    ","##    ##   ","##     ##  "],
    [" ######    ","##    ##   ","##         "," ######    ","      ##   ","##    ##   "," ######    "], 
    ["########   ","   ##      ","   ##      ","   ##      ","   ##      ","   ##      ","   ##      "],   
    ["##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  ","##     ##  "," #######   "], 
    ["##     ##  ","##     ##  ","##     ##  ","##     ##  "," ##   ##   ","  ## ##    ","   ###     "],   
    ["##      ## ","##  ##  ## ","##  ##  ## ","##  ##  ## ","##  ##  ## ","##  ##  ## "," ###  ###  "], 
    ["##     ##  "," ##   ##   ","  ## ##    ","   ###     ","  ## ##    "," ##   ##   ","##     ##  "],
    ["##    ##   "," ##  ##    ","  ####     ","   ##      ","   ##      ","   ##      ","   ##      "],   
    ["########   ","     ##    ","    ##     ","   ##      ","  ##       "," ##        ","########   "],
]

char = input("Enter a char = ").lower()

alpha = " abcdefghijklmnopqrstuvwxyz"

index = alpha.find(char)

for i in range(7):
    print(pattern[index][i])
    