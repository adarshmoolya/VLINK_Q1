elements = []
num = int(input("Enter the number of Words:"))
num = num+1
if num > 0:
    for i in range (num) :
        elements.append(input("Enter the elements:"))
    elements.sort(key = len)
    print(elements)
else:
    print("Inavlid Input")
