# RemoveFasta
A script to remove a list of sequences from a fasta file.

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- requirements -->
## Requirements

This script has been tested with Python 2.7 and 3 and should work with either.
The script requires a fasta file.  The fasta file can be compressed with gzip.
The script requires a text file with the header of the sequence(s) to be removed from the fasta file.  The header must exactly match.  This file can be compressed with gzip.

<!-- usage -->
## Usage

python remove.seq.v2.py -fasta file.fasta -remove remove.txt

To see the usage and get futher information: python remove.seq.v2.py -h

<!-- license -->
## License 

Distributed under the MIT License.
