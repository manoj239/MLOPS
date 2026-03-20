a = "hello"
b = "world"
# Concatenation
concatenated_string = a + " " + b
print(f"Concatenation: {concatenated_string}")
# Repetition
repeated_string = (a + " " )* 3
print(repeated_string)
print(a[0])
print(a.index('o')) #index number
print(a[-1])
print("----------------------------------")
a = "Hello world"
print(a[1:7])
print(f"Characters with a step of 2: {a[::2]}")
#print("----------------------------------You will get known error as strings are immutable")
a[2]='m'
#print(a)

# upper()	Converts to uppercase	"hi".upper() → 'HI'
# lower()	Converts to lowercase	"HI".lower() → 'hi'
# capitalize()	Capitalizes first letter	"hello".capitalize()
# strip()	Removes spaces from ends	" hi ".strip()
# replace(old, new)	Replace substring	"hat".replace("h", "c")
# split()	Splits string into list	"a,b,c".split(",")
# join()	Joins elements with string separator	",".join(['a','b'])
# find()	Finds index of substring	"hello".find("l")
# count()	Counts occurrences of substring	"hello".count("l")