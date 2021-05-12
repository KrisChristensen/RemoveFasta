##########################################################
### Import Necessary Modules

import argparse                       #provides options at the command line
import sys                       #take command line arguments and uses it in the script
import gzip                       #allows gzipped files to be read
import re                       #allows regular expressions to be used

##########################################################
### Command-line Arguments
parser = argparse.ArgumentParser(description="A script to remove scaffolds/contigs from fasta file using a contamination file")
parser.add_argument("-fasta", help = "The location of the fasta file", default=sys.stdin, required=True)
parser.add_argument("-remove", help = "File with scaffolds/contigs to remove (one per line, must match fasta)", default=sys.stdin, required=True)
args = parser.parse_args()

class Variables():
    remove = {}

class OpenFile():
    ### Opens the file either using a regular mechanism or opens it after uncompressing the data
    def __init__ (self, cb, t):
        """Opens a file (gzipped accepted)"""
        if re.search(".gz$", cb):
            self.filename = gzip.open(cb, 'rb')
        else:
            self.filename = open(cb, 'r')
        if t == "fasta":
            FastaFile(self.filename)
        else:
            Remove(self.filename)
            
class Remove():
    def __init__ (self, f):
        """Removes sequences from the fasta file"""
        self.filename = f
        for line in self.filename:
            try:
                line = line.decode('utf-8')
            except:
                pass        
            line = line.rstrip('\n')
            Variables.remove[line] = 1
        self.filename.close()

class FastaFile():
    def __init__ (self, f):
        """Removes sequences from the fasta file"""
        self.filename = f
        self.toRemove = "no"
        self.removed = 0
        self.number_scaffolds = 0
        for line in self.filename:
            try:
                line = line.decode('utf-8')
            except:
                pass        
            line = line.rstrip('\n')
            if re.search("^\>", line):
                self.header = line[1:]
                if self.header in Variables.remove:
                    sys.stderr.write("\tremoving {}\n".format(self.header))
                    self.toRemove = "yes"
                    self.removed += 1
                else:
                    print (">{}".format(self.header))
                    self.toRemove = "no"
                self.number_scaffolds += 1
            elif re.search("\w", line):
                if self.toRemove == "no":
                    print ("{}".format(line))
        sys.stderr.write("\nFound {} scaffolds/contigs and removed {} \n\n".format(self.number_scaffolds, self.removed))
        self.filename.close()

if __name__ == '__main__':
    open_file2 = OpenFile(args.remove, "remove")
    open_file2 = OpenFile(args.fasta, "fasta")
