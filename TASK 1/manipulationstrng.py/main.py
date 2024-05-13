#manupulation of strings
string1="hello world"
string2="WELCOME TO PYTHON"
string3="this is first program"
string1_uppercase=string1.upper()
print(string1_uppercase)
string2_lowercase=string2.lower()
print(string2_lowercase)
#strip
string3_no_space=string3.strip()
print(string3_no_space)
#spilt of string
string1_split=string1.split(",")
print(string1_split)
#join of string
string2_join="".join(string2)
print(string2_join)
#replaceing of string
string3_python=string3.replace("this is", "python")
print(string3_python)
#length of string
print(len(string2))