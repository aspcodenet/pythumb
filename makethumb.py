from PIL import Image
from argparse import ArgumentParser
import os
import sys

argParser = ArgumentParser() 
argParser.add_argument("-s", "--source", help="filename large file", type=str) 
argParser.add_argument("-t", "--target", help="filename small file", type=str) 
argParser.add_argument("-x", "--x", help="width in pixels",type=int, default=100) 
argParser.add_argument("-y", "--y", help="height in pixels",type=int,default=100) 
args = argParser.parse_args() 

if not args.source:
    print("Ange source file")
    sys.exit(1)

if not args.target:
    print("Ange target file")
    sys.exit(1)


if not os.path.isfile(args.source):
    print("Ingen sån fil")
    sys.exit(1)


image = Image.open(args.source)
image.thumbnail((args.x,args.y))  
image.save(args.target)


sys.exit(0)

