with open('data/1OLG.pdb', 'r') as f:
    f_lines = f.readlines()
    print('In the with block, is the file closed?', f.closed)

print('Our of the with block, is the file closed?', f.closed)

print(f_lines[:3])
