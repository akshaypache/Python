def barakhadi():
    """Print all hindi barakhadi"""
    try:
        from prettytable import PrettyTable
    except:
        import os 
        os.system("pip install prettytable")
        from prettytable import PrettyTable

    vowels = ["A", "a", "i", "ee", "u", "oo", "e", "ai", "o", "au", "am", "an"]
    table = PrettyTable( vowels )
    letters = ["k", "kh", "g", "gh", "ch", "chh", "j", "jh", "t", "th", "d", "d", "n", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "w", "sh", "sh", "s", "h", "ksh", "gy"]
    for char in letters:
        list = []
        for i in vowels:
            list.append( char + i )
        table.add_row( list )
    barakhadi = str( table ).upper() 
    return barakhadi

def tables(Start_point,End_point):
    """Print Tables from starting point to end point"""
    try:
        from prettytable import PrettyTable
    except:
        import os 
        os.system("pip install prettytable")
        from prettytable import PrettyTable
    nums = [i for i in range(Start_point,End_point+1)]
    myTable = PrettyTable(nums)
    for i in range(1,11):
        list = []
        for j in nums:
            list.append(i * j)
        myTable.add_row(list)
    return myTable

def romanToDecimal(romanNumeral):
    """Roman value to decimal value"""
    romanNumeral = romanNumeral.upper()
    tallies = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum

def textAnalyse(text):
    """Text analyse returns the dictionary of every char how many percentage of string taking"""
    dictionary = {}
    def count_char(text, char):
        count = 0
        for c in text:
            if c == char:
                count +=1
        return count
    text = text.lower()
    for char in "abcdefghijklmnopqrstuvwxyz":
        percent = 100 * count_char(text, char)/len(text)
        per = round(percent,2)
        if(per != 00.00):
            dictionary.update({f"{char}": f"{per}%"})
    return dictionary

def mean(word):
    from words import wordsDic
    mean = wordsDic[word]
    return mean 

def chemEleInfo(ElementSymbol):
    """All info about periodic table element"""
    ElementSymbol = ElementSymbol.title()
    from words import eleDict
    info = eleDict[ElementSymbol]
    return info

def AllChemElements():
    """all elements of periodic table"""
    from words import eleDict
    list = []
    for i in eleDict:
        list.append(i)
    return list 

def CountAll(string):
    """how many chars are lower, upper, digits, special char and space in string"""
    lower = upper = number = symbol = space = 0
    for char in string:
        if char.islower():
            lower = lower + 1
        elif char.isupper():
            upper = upper + 1
        elif char.isdigit():
            number = number+ 1
        elif char== " ":
            space = space + 1
        else:
            symbol = symbol + 1
    return {"lower":lower, "upper":upper,"number":number, "symbol":symbol,"space":space}

def isEven(a):
    """check number is Even"""
    if a%2==0:
        return True
    else:
        return False 
    
def isOdd(a):
    """check number is Odd"""
    if a%2!=0:
        return True
    else:
        return False 

def factorial(a):
    """return factorial of given number"""
    if(a<0):
        return -1
    else:
        ans = 1
        for i in range(1,a+1):
            ans = ans*i
        return ans

def isArmstrongNumber(num):
    lenNum = len(num)
    sum = 0
    for i in range(lenNum):
        sum = sum + int(num[i])**lenNum
    if(sum==int(num)):
        return True
    else:
        return False

def fibbonacciSequence(num):
    """provide list upto Nth position"""
    num1 = 0
    num2 =  1
    count = 0
    list = []
    if num < 0:
        return "Invalid Value"
    elif num == 1 or num==0:
        list.append(num1)
    else:
        while count < num:
            list.append(num1)
            temp = num1 + num2
            num1 = num2
            num2 = temp
            count += 1
    return list

def isPalindrome(string):
    """If string is Palindrome return true"""
    st = str(string).lower()
    if st==st[::-1]:
        return True 
    else:
        False

