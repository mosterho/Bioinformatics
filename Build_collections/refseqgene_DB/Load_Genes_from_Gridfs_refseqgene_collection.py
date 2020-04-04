
## Build a single gene collection
## from the refseq NCBI files

## read from the refseqgene files from NCBI, upload to a single
## "regular" collection refseqgene_file

import sys
from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.refseqgene
fs_forread  = gridfs.GridFSBucket(db)
fs_forwrite = db.refseqgene_file  # for writing to a new file

## delete any entries in refseqgene_file before starting
print('perform "delete_many" on existing refseqgene collection')
fs_forwrite.delete_many({})

wrk_accession_break = ''
first_read = False

## Perform "find" and "read" to loop through approx. 22 refseqgene GridFS files
for fs_find in fs_forread.find({}):
    fs_read = fs_find.read()
    print('fs_read: ', fs_read[:100])
    # Decode binary ddata and split based on newline character
    fs_read_decode = fs_read.decode()
    fs_read_decode_splits = fs_read_decode.split("\n")
    # read through list (created by "split"), concatenate
    # nucleotide data, write a single document based on Gene number
    # note: "first_read" is just a "first row read" indicator
    for x_read in fs_read_decode_splits:
        if(x_read[:1] == ">"):
            if(first_read is True):
                Nucleotide_encoded = write_data.encode()
                fs_forwrite.insert_one({"Taxon":"9606", "Organism":"Homo sapiens", "accession_nbr":accession_nbr, "gene": gene_abbrev, "Description":description, "Nucleotides":Nucleotide_encoded})
                print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
            else:
                first_read = True
            accession_nbr = x_read[1:10]
            # Use REGEX to find gene abbreviations within description, e.g. (OR6K3)
            gene_abbrev_list = re.findall('(?<=[(]).+?(?=[)])', x_read)
            # looks like some entries have two or more gene accession.
            # For now, find the last entry. May put this in an array in the future.
            for x in gene_abbrev_list:
                gene_abbrev = x
            description = x_read[13:]
            write_data = x_read  # note the use of "=" here and "+=" further down
        else:
            write_data += x_read
    # end of file, write last document, continue with next refseqgene GridFS file
    Nucleotide_encoded = write_data.encode()
    fs_forwrite.insert_one({"accession_nbr":accession_nbr, "gene": gene_abbrev, "Description":description, "Nucleotides":Nucleotide_encoded})
    print('accession: ', accession_nbr, 'gene abbrev: ', gene_abbrev, 'description: ', description)
