#!/bin/bash
#create dissassemblies for all exe with flipped bits

objdump $1 -D -M intel-mnemonic > original;

for f in *.exe;
  do
    objdump $f -D -M intel-mnemonic > $f.dmp;
    diff original $f.dmp > $f.diff;
  done