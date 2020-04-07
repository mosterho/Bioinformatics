
## Build a single gene collection
## from the refseq NCBI files
# Example data from NCBI
#>NP_000005.2 alpha-2-macroglobulin isoform a precursor [Homo sapiens]
#MGKNKLLHPSLVLLLLVLLPTDASVSGKPQYMVLVPSLLHTETTEKGCVLLSYLNETVTVSASLESVRGNRSLFTDLEAE
#NDVLHCVAFAVPKSSSNEEVMFLTVQVKGPTQEFKKRTTVMVKNEDSLVFVQTDKSIYKPGQTVKFRVVSMDENFHPLNE

import sys
from pymongo import MongoClient
import gridfs, re

def fnc_writedata(arg_writedata, arg_gi, arg_ref, arg_description):
    AA_encoded = arg_writedata.encode()
    fs_forwrite.insert_one({"Taxon":"9606", "Organism":"Homo sapiens", "GI":arg_gi, "ref": arg_ref, "Description":arg_description, "Amino_acids":AA_encoded})
    #print("GI ", arg_gi, "ref ", arg_ref, "Description ", arg_description)


client = MongoClient('mongodb')
db = client.protein
fs_forread  = gridfs.GridFSBucket(db)
fs_forwrite = db.protein_file  # for writing to a new file

## delete any entries in refseqgene_file before starting
print('perform "delete_many" on existing protein collection')
fs_forwrite.delete_many({})

first_read = False

for fs_find in fs_forread.find({}):
    fs_read = fs_find.read()
    print('Begin writing to Protein file... ')
    #
    fs_read_decode = fs_read.decode()
    fs_read_decode_splits = fs_read_decode.split("\n")
    for x_read in fs_read_decode_splits:
        ## if ">" encountered, this is a new document, write previous GI first
        ## Also Test if this is the first row read from the file ("first_read" flag)
        ##    set the "first_read" flag to True after first row is read
        if(x_read[:1] == ">"):
            if(first_read is True):
                fnc_writedata(write_data, gi_nbr, ref_abbrev, description)
            else:
                first_read = True
            wrk_fieldbreak = x_read.split('|')
            gi_nbr = (wrk_fieldbreak[1])
            ref_abbrev = wrk_fieldbreak[3]
            description = wrk_fieldbreak[4][1:]
            write_data = x_read  # Note that this is "=", but non-breaking data read is "+="
        else:
            write_data += x_read
            ## At end of file, write last document, then continue reading bucket/file
    fnc_writedata(write_data, gi_nbr, ref_abbrev, description)
    print('Finished writing to Protein file... ')
