name=input("enter the name : ")
words = name.split(" ")
short_name = " ".join([word[0]for word in words])
print("abbreviated form is :" +short_name)