#"Falsy in python"
#False
#None
#[]
#{}
#""
#set()
#0
#0.0

#evertything other than these is treated True in python
#these allow to check if empty list/dicts etc

s = ""
first_char = s and s[0]
print("empty string:", first_char)

s = "hm"
first_char = s and s[0]
print(first_char)  