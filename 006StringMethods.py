# String method To change String

s1="Hi I am Pratik bera. I am from Kolkata."

slower=s1.lower()
supper=s1.upper()
scapitalize=s1.capitalize()
stitle=s1.title()
sswapcase=s1.swapcase()
print("Lower =",slower)
print("Upper =",supper)
print("capitalize =",scapitalize)
print("title = ",stitle)
print("Opposite = ",sswapcase)


# The Function to check the string validations
print("\n validations prints")
s2="***Hello , Good *Morning all**"
print("s2 = ",s2)

sdigit="4566"
print(sdigit.isdigit())
print(s2.isdigit())

print(s2.isalpha())
print(s2.isalnum())

print(s2.strip("*"))
print(s2.lstrip("*"))
print(s2.rstrip("*"))

s3="Pratik Bera"
print(s3.count("a"))
print(s3.index("a"))
print(s3.replace("Bera","Das"))
print(s3)

print(s3.startswith("P"))
print(s3.endswith("a"))





