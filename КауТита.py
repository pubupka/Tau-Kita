string = input()
s = string.split(" ")
f = []


def translate(array):
    final = []
    mid = len(array) // 2
    if len(array) == 1:
        return array
    elif len(array) % 2 == 0:
        for i in range(mid):
            final.insert(0, array[i])
            final.insert(0, array[-i-1])
    else:
        for j in range(mid):
            final.insert(0, array[-j - 1])
            final.insert(0, array[j])
        final.insert(0, array[mid])
    return final


s_t = translate(s)

for i in range(len(s_t)):
    print("".join(translate(list(s_t[i]))), end=" ")