with open('1.txt', encoding="utf-8") as file:
    text1 = file.read()
    cnt1 = text1.count('\n') + 1
with open('2.txt', encoding="utf-8") as file:
    text2 = file.read()
    cnt2 = text2.count('\n') + 1
with open('3.txt', encoding="utf-8") as file:
    text3 = file.read()
    cnt3 = text3.count('\n') + 1

text = [[str(cnt1), text1, '1.txt'], [str(cnt2), text2, '2.txt'], [str(cnt3), text3, '3.txt']]
text.sort()

# print(text)
with open('4.txt', 'w', encoding="utf-8") as file:
    for i in text:
        file.write('\n'.join(i))
        file.write('\n')
