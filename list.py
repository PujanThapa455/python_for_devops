options=["male","female","other","none"]
check = input("Enter the value to check:")
if check in options:
    print("Yes,its present")
else:
    print("No,its not present")
    
print(options)
print(type(options))
print(len(options))
print(options[1])
print(options[0:2])
print(options[:1])
print(options[2:])
print(options[-1])
