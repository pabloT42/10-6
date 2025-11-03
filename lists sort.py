print(" type words until they type 'stop':")
num = 0
scoresList = []
while num != "stop":
    num = input("type words:")
    if num != "stop":
        scoresList.append(num)
print("words you typed:")
scoresList.sort()
print(scoresList)
