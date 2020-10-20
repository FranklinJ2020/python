print('Exercise 7.1')
fname = input('What file should we open? ')

try:
    fh = open(fname)
except:
    print(fname, 'is not found. Please enter a valid file.')
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())
