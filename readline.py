import os

if os.path.isfile('mastery.txt'):
    print('Sorry, file exists.')
else:
    with open('mastery.txt', 'w') as f:
        f.write("This is my file")
        f.write("There are many like it, but this one is mine.")
        f.write("I must master my file like I must master my life.")

with open('data/1OLG.pdb', 'r') as f:
    for i, line in enumerate(f):
        print(line.rstrip())
        if i >= 10:
            break

with open('gimme_phi.txt', 'w') as f:
    f.write('The golden ratio φ is = ')
    f.write('{phi:.8f}'.format(phi=1.61803398875))
