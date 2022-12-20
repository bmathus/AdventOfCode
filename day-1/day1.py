file1 = open('input.txt', 'r')
lines = file1.readlines()

biggest_elf = 0
current_elf = 0

top_tree_total = [0,0,0]

for idx in range(len(lines)):
    if len(lines[idx]) == 1:
        if current_elf > min(top_tree_total):
            top_tree_total.remove(min(top_tree_total))
            top_tree_total.append(current_elf)
        current_elf = 0
        continue

    current_elf = current_elf + int(lines[idx])

print(sum(top_tree_total))
        

    
