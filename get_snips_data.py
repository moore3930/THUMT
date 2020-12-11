

input_file = "/Users/wudi39/github/robust-NLU/data/snips/test/data"
output_file_1 = input_file + '.query'
output_file_2 = input_file + '.slot'

fout1 = open(output_file_1, 'w')
fout2 = open(output_file_2, 'w')

for line in open(input_file):
    line = line.strip()
    line_array = line.split('\t')
    label_lst = []
    b_lable = ""
    for w, l in zip(line_array[0].split(' '), line_array[1].split(' ')):
        if l == 'O':
            continue

        if l.startswith('B-'):
            label_lst.append(l)
            label_lst.append(w)
        else:
            label_lst.append(w)

    fout1.write(line_array[0] + '\n')
    fout2.write(' '.join(label_lst) + '\n')
    print(line_array[0])
    print(' '.join(label_lst))

fout1.flush()
fout2.flush()
fout1.close()
fout2.close()


