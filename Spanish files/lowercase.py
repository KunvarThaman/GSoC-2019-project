import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-inf", "--input_file", type=str, help="Name of\
                    input file")
parser.add_argument("-t", "--timing", default=0, type=int, help="Option to decide whether\
                    to include timing info in output")
args = parser.parse_args

fin = open(args.input_file)
fout = open(outfile, "w+")

for line in f:
	ine = line.decode('utf-8').lower()
	fout.write(line)
	
fin.close()
fout.close()
	
