import re
sourcefile = 'cornell-movie-dialogs-corpus/movie_lines.txt'
output = 'out/movie_lines-alphabetised.txt'

# with open()

# 1. strip all formatting from start 
with open(sourcefile, encoding="utf8", errors='ignore') as f:
    for line in f:

        iter = re.finditer(r"\+\+\+\$\+\+\+\ ", line)
        indices = [m.start(0) for m in iter]
        n = indices[len(indices)-1]+8
        q = line[n:len(line)]
        for i, c in enumerate(q):
            if c.isalpha() or c.isdigit():
                q = q[i:len(q)]
                break
        print (q)

        with open(output,'a') as f2:
            f2.write(q)

# this line. runs via UNIX terminal
!sort out/movie_lines-alphabetised.txt -o out/movie_lines-alphabetised.txt
