def get_atom_num(lines):
    inp = lines[6].split()
    atom_num = int(inp[0])
    return atom_num

def print_every_poscar(lines,N):
    num_poscar = len(lines)/N           ####number of poscars
    j = 0
    k = 0
    for i in range(0,len(lines)):
        if i%N == 0:
            j = j + 1
            if j > 1000:
                k = k + 1
                outfile = open('POSCAR-%s' % k, 'w')
        if j > 1000:
            outfile.write(str(lines[i]))
#	if j >= 5:
#	    break    
    return 0
		
#filepath = "D:\\study\\data\\NPT\\test\\XDATCAR"
#poscar_path = "D:\\study\\data\\NPT\\test\\test\\POSCAR"
f = open("XDATCAR", 'r')
lines = f.readlines()

atom_num = get_atom_num(lines)
N = atom_num + int(8)         # the poscar
print_every_poscar(lines,N)