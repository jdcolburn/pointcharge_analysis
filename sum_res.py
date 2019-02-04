#!/usr/bin/env python

import re

residue_file = open("residuelist", "r")
for entry in residue_file:
    index = (entry.split())
    score_file = open("py_output.out", "r")
    file_contents = score_file.read()
    matching_lines = re.findall(index[0] +
                                '[ \t]+' + index[1] +
                                '[ \t]+' + index[2] +
                                '[ \t]+' + '[\w]+' +
                                '[ \t]+' + '[-]*[\d]+\.[\d]+', file_contents)
    if matching_lines:
        scores = []
        for line in matching_lines:
            match = line.split()
            scores.append(float(match[4]))
        print(index[0],
              "	", index[1],
              "	", index[2],
              "	", '{:.6f}'.format(sum(scores)))
    else:
            print("no match")
