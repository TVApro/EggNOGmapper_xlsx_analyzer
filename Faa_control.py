#!/home/lab330/anaconda3/bin/python3
import sys, os
def fasta_obtain(text):
        from re import sub
        fasta_sorted_list = {}
        fasta_list = sorted(text.split(">"), key=len, reverse=True)
        for i in fasta_list:
                if i != ' ' and i != '':
                        end = i.find("\n")
                        fasta_name = '>'+sub('\n', '', i[:end])
                        fasta_sequence = sub('\n', '', i[end:])
                        fasta_sorted_list[fasta_name]=fasta_sequence
        return len(fasta_sorted_list)

path = os.getcwd()
file1 = sys.argv[1]
file2 = sys.argv[2]

with open(path+'/'+file1, 'r') as file:
        text1 = file.read()
with open(path+'/'+file2, 'r') as file:
        text2 = file.read()
n = fasta_obtain(text1)
m = fasta_obtain(text2)

print('В файл', file1, 'содержится', n, 'аннотаций')
print('В файл', file2, 'содержится', m, 'аннотаций')
        

