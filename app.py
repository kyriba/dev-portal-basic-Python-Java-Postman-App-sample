
# insert the copied code below this line


chars = list(data.decode("utf-8"))
for i in range(len(chars)):
 if chars[i] == "{":
    chars[i] = chars[i].replace("{", "\n{")
 if chars[i] == ",":
    chars[i] = chars[i].replace(",", ",\n")

print("".join(chars))