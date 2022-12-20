file1 = open('input.txt', 'r')
backpacks = file1.readlines()
types = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))

#priority sum
priority_sum = 0

for idx in range(len(backpacks)):
    backpacks[idx] = backpacks[idx].replace("\n","")

    left_pack = set(backpacks[idx][:len(backpacks[idx])//2])
    right_pack = set(backpacks[idx][len(backpacks[idx])//2:])

    priority_sum += types.index(list(left_pack & right_pack).pop()) + 1
    
print(priority_sum)








