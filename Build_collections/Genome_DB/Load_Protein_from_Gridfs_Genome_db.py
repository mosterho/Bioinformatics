###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient
import gridfs, re

client = MongoClient('mongodb')
db = client.Genome
fs_forread = gridfs.GridFSBucket(db)
fs_forwrite = db.Genome_proteins_file  # for writing to a new file

## delete any entries in refseqgene_file before starting
print('perform "delete_many" on existing Genome_proteins_file collection')
fs_forwrite.delete_many({})

# Retrieve data from "9606_Genome_protein"
for fs_datafind in fs_forread.find({"filename":"9606_Genome_protein"}):
    dataread = fs_datafind.read()
    #print('dataread from read() is: ', dataread[:1000])
    ## Decode data read
    x_decoded = dataread.decode()
    # split off proteins into individual entries in a list
    match_object = x_decoded.split('>')
    for new_list in match_object:
        #print('New_list match object: ', new_list)
        # create a list of a single protein, removing "\n" character
        wrk_protein_data = new_list.split('\n')
        # "pop" the first line to retrieve accession and description,
        # this will leave remaining protein data in wrk_protein_data
        wrk_first_line = wrk_protein_data.pop(0)
        # REGEX is probably better at finding "accession" and
        # "description"... just trying "find"
        wrk_find = wrk_first_line.find('.')
        wrk_find2 = wrk_first_line.find(' ', wrk_find)
        wrk_accession = wrk_first_line[:wrk_find2]
        # Determine description based on last '.## ' (note the space) found for accession#
        wrk_description = wrk_first_line[wrk_find2 + 1:]
        ## Build/concatenate protein data into single data field and encode
        wrk_tmpdata = ''
        for tmp_data in wrk_protein_data:
            wrk_tmpdata += tmp_data
        wrk_dataforwrite = wrk_tmpdata.encode()
        ## Inset data to collection
        #print("accession_nbr:", wrk_accession, "Description:", wrk_description, 'data:', wrk_dataforwrite[:100])
        fs_forwrite.insert_one({"Taxon":"9606", "Organism":"Homo sapiens", "accession_nbr":wrk_accession, "Description":wrk_description, "AA":wrk_dataforwrite})

print('Finished writing Genome_protein...')
