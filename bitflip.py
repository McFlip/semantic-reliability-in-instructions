import argparse

parser = argparse.ArgumentParser()
parser.add_argument("infile", help="input file")
parser.add_argument("offset", help="offset into file in bytes", type=int)
parser.add_argument("numBytes", help="number of bytes to process", type=int)
parser.add_argument("directory", help="directory to dump all output")
args = parser.parse_args()

maskList = [0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80]

with open(args.infile, 'rb') as infile:
  original = bytes(infile.read())
for byteOffset in range(args.numBytes):
  for bitOffset in range(8):
    copy = bytearray(original)
    fileOffset = args.offset + byteOffset
    print "offset : {0:#x}".format(fileOffset)
    mask = maskList[bitOffset]
    print "mask : {0:b}".format(mask)
    print "original : {0:b}".format(copy[fileOffset])
    print "original : {0:#x}".format(copy[fileOffset])
    copy[fileOffset] ^= mask
    print "flipped  : {0:b}".format(copy[fileOffset])
    print "flipped  : {0:#x}".format(copy[fileOffset])
    fname = "0x"
    for i in range(args.numBytes):
      fname = fname + "{0:x}".format(copy[args.offset + i])
    path = args.directory + "/" + fname + ".exe"
    print "path : " + path
    with open(path, 'wb') as outfile:
      outfile.write(copy)
