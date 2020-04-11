###
# Compare the protein collections in the "Genome" database against the "protein" database
# Attempt to use cursors with both collections to compare accession numbers.

#### WIP, see version 2 that is complete. This will load the collections
#### into lists and then use the indexes to move through the accession numbers

from pymongo import MongoClient

#import gridfs, re

client = MongoClient('mongodb')
db_genome = client.Genome
db_protein = client.protein

fs_forread_genome = db_genome.Genome_proteins_file
fs_forread_protein = db_protein.protein_file

fs_genome_cursor = fs_forread_genome.find({},{ "accession_nbr": 1}).sort("accession_nbr")
fs_protein_cursor = fs_forread_protein.find({},{ "ref": 1}).sort('ref')

## Perform initial setup for cursors
finale = False
counter_match = 0
counter_genome_mismatch = 0
counter_protein_mismatch = 0
genome_cursor_doc = fs_genome_cursor.next()
protein_cursor_doc = fs_protein_cursor.next()
## Loop through cursors until finale is True
while finale == False:
    wrk_genome_nbr = genome_cursor_doc.get("accession_nbr")
    wrk_protein_nbr = protein_cursor_doc.get("ref")
    print('genome cursor:',  wrk_genome_nbr, 'protein cursor:', wrk_protein_nbr)
    if(wrk_genome_nbr  == wrk_protein_nbr):
        counter_match += 1
        genome_cursor_doc = fs_genome_cursor.next()
        protein_cursor_doc = fs_protein_cursor.next()
    elif(wrk_genome_nbr < wrk_protein_nbr):
        counter_genome_mismatch += 1
        genome_cursor_doc = fs_genome_cursor.next()
    else:
        counter_protein_mismatch += 1
        protein_cursor_doc = fs_protein_cursor.next()
print('This worked')
print('matched:', counter_match)
print('mis-matched genome:', counter_genome_mismatch)
print('mis-matched protein:', counter_protein_mismatch)
