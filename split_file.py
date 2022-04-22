with open("sampleData200k.txt",'r') as file:
    lines = file.readlines()

# with open("sampleData200k_A.txt",'w') as file:
#     for line in lines[:int(len(lines)/4)]:
#         file.write(line)

# with open("sampleData200k_B.txt",'w') as file:
#     for line in lines[int((len(lines)/4)*1):int((len(lines)/4)*2)]:
#         file.write(line)
        
# with open("sampleData200k_C.txt",'w') as file:
#     for line in lines[int((len(lines)/4)*2):int((len(lines)/4)*3)]:
#         file.write(line)

# with open("sampleData200k_D.txt",'w') as file:
#     for line in lines[int((len(lines)/4)*3):int((len(lines)/4)*4)]:
#         file.write(line)

with open("sampleData200k_20k.txt",'w') as file:
    for line in lines[int((len(lines)/10)*9):int((len(lines)/10)*10)]:
        file.write(line)

with open("sampleData200k_10k.txt",'w') as file:
    for line in lines[:int(len(lines)/20)]:
        file.write(line)

        