import random

input_file = "/Users/wudi39/github/robust-NLU/THUMT/data/snips/valid/data.slot"
output_file = "/Users/wudi39/github/robust-NLU/THUMT/data/snips/valid/domain.label"

fout = open(output_file, 'w')

for line in open(input_file):
    line = line.strip()
    fout.write('1\n')

fout.flush()
fout.close()

