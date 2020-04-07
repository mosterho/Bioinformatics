###
# open NCBI upload files in the Gridfs format
# write to collections

from pymongo import MongoClient

class cls_genome_protein_accs:
    def __init__(self):
        self.genome_acc = []
        self.genome_count = 0
        self.protein_acc =[]
        self.protein_count = 0
    def fct_genome_store(self, arg_genome_cursor):
        self.genome_acc.append(arg_genome_cursor)
        self.genome_count += 1
    def fct_protein_store(self, arg_protein_cursor):
        self.protein_acc.append(arg_protein_cursor)
        self.protein_count += 1

client = MongoClient('mongodb')
db_genome = client.Genome
db_protein = client.protein

fs_forread_genome = db_genome.Genome_proteins_file
fs_forread_protein = db_protein.protein_file

cls_working = cls_genome_protein_accs()

for fs_genome_cursor in fs_forread_genome.find({},{ "accession_nbr": 1}).sort("accession_nbr"):
    cls_working.fct_genome_store(fs_genome_cursor.get("accession_nbr"))
for fs_protein_cursor in fs_forread_protein.find({},{ "ref": 1}).sort('ref'):
    cls_working.fct_protein_store(fs_protein_cursor.get("ref"))

print('genome counter:', cls_working.genome_count, 'genome list "length":', len(cls_working.genome_acc))

## Perform initial setup for cursors
finale = False
counter_match = 0
counter_genome_mismatch = 0
counter_protein_mismatch = 0
wrk_genome_nbr = 0
wrk_protein_nbr = 0
## Loop through cursors until finale is True
while finale == False:
    print('genome cursor:',  cls_working.genome_acc[wrk_genome_nbr], 'protein cursor:', cls_working.protein_acc[wrk_protein_nbr])
    if(cls_working.genome_acc[wrk_genome_nbr]  == cls_working.protein_acc[wrk_protein_nbr]):
        counter_match += 1
        wrk_genome_nbr += 1
        wrk_protein_nbr += 1
    elif(cls_working.genome_acc[wrk_genome_nbr] < cls_working.protein_acc[wrk_protein_nbr]):
        counter_genome_mismatch += 1
        wrk_genome_nbr += 1
    else:
        counter_protein_mismatch += 1
        wrk_protein_nbr += 1
    if(wrk_genome_nbr >= cls_working.genome_count or wrk_protein_nbr >= cls_working.protein_count):
        finale = True
        break

#print('This worked')
print('matched:', counter_match)
print('mis-matched genome (genome without matching protein):', counter_genome_mismatch)
print('mis-matched protein (protein without matching genome):', counter_protein_mismatch)
