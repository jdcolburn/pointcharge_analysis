#!/usr/bin/env python

import re

geom_file = open("geometry.pdb", "r")
for entry in geom_file:
    match = re.search('FE', entry)
    if match:
        iron = (entry.split())
        fe_coords = [iron[5], iron[6], iron[7]]
        break

pc_file = open("pointcharges.xyz", "r")
for pc_entry in pc_file:
    point_charge = (pc_entry.split())
    charge = '{:.4f}'.format(round(float(point_charge[0]), 6))
    coords = ['{:.3f}'.format(round(float(point_charge[1]), 6)),
              '{:.3f}'.format(round(float(point_charge[2]), 6)),
              '{:.3f}'.format(round(float(point_charge[3]), 6))]
    geom_file = open("geometry.pdb", "r")
    for geom_entry in geom_file:
        match = re.search('[ \t]+' + coords[0] +
                          '[ \t]+' + coords[1] +
                          '[ \t]+' + coords[2], geom_entry)
        if match:
            atom = (geom_entry.split())
            residue_name = (atom[3])
            residue_id = (atom[4])
            atom_name = (atom[2])
            segment_name = (atom[10])
            vector = [float(coords[0])-float(fe_coords[0]),
                      float(coords[1])-float(fe_coords[1]),
                      float(coords[2])-float(fe_coords[2])]
            sum_squares = (vector[0]**2 + vector[1]**2 + vector[2]**2)
            length = (sum_squares**(1/2))
            score = (float(charge)/length)
            print(segment_name,
                  "	", residue_name,
                  "	", residue_id,
                  "	", atom_name,
                  "	", '{:.6f}'.format(score))
            break
