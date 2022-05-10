colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
arr = []
a = input()
b = input()
c = input()

arr.append(colors.index(a))
arr.append(colors.index(b))
arr.append(10 ** colors.index(c))

print(int(str(arr[0]) + str(arr[1])) * arr[2])