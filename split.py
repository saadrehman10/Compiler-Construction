
character = []

# Read file
with open('usercode.txt','r') as f:
    content = f.read()

    for i in range(0,len(content)):
        if content[i] == ' ':
            pass
        else:
            character.append(content[i])
    # print(content)

print(character)