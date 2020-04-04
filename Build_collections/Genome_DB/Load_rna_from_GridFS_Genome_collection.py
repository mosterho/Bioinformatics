##
# Import rna from GridFS file
# sample data, use this for REGEX searches/patterns esp. first line
# >NM_000018.4 Homo sapiens acyl-CoA dehydrogenase very long chain (ACADVL), transcript variant 1, mRNA
# AGAGCTGGGTCAGAGCTCGAGCCAGCGGCGCCCGGAGAGATTCGGAGATGCAGGCGGCTCGGATGGCCGCGAGCTTGGGG
# CGGCAGCTGCTGAGGCTCGGGGGCGGAAGCTCGCGGCTCACGGCGCTCCTGGGGCAGCCCCGGCCCGGCCCTGCCCGGCG

from pymongo import MongoClient
import gridfs, re, sys

client = MongoClient("mongodb")
db = client.Genome
fs_forread = gridfs.GridFSBucket(db)
fs_forwrite = db.Genome_rna_file

## Remove any existing "Genome_rna_file" entries
print('Deleting entries from collection "Genome_rna_file"...')
fs_forwrite.delete_many({})

print('Processing Genome rna GridFSBucket data...')
wrk_searchforacc = re.compile('.._[0-9]*\.[0-9]*')  # NM_000018.4
wrk_searchfordesc = re.compile('(?<=[ ]).*')  # Homo sapiens acyl-CoA dehydrogenase very long chain (ACADVL), transcript variant 1, mRNA
wrk_searchforgene = re.compile('(?<=[(]).*(?=[)])') # ACADVL
wrk_searchforrnatype = re.compile('\w*$') # mRNA

#print('acc:', wrk_searchforacc, 'desc:', wrk_searchfordesc, 'gene:', wrk_searchforgene)

for tmp_forread in fs_forread.find({"filename":"9606_Genome_rna"}):
    wrk_read = tmp_forread.read()
    ## decode the data read
    wrk_read_decoded = wrk_read.decode()
    ## Split data into rna chunks/lists based on ">"
    wrk_read_decoded_split = wrk_read_decoded.split('>')
    ## Split data based on newline
    for loop1 in wrk_read_decoded_split:
        loop1_data = loop1.split('\n')
        ## POP first line to obtain key data. Loop through list,
        ## then assemble/concatenate rna nucleotides into single document
        wrk_pop = loop1_data.pop(0)
        #print('wrk_pop:', wrk_pop, '\nloop1_data:', loop1_data)
        if(wrk_pop != ''):
            tmp_acc = re.findall(wrk_searchforacc, wrk_pop)
            wrk_acc = tmp_acc[0]
            tmp_desc = re.findall(wrk_searchfordesc, wrk_pop)
            wrk_desc = tmp_desc[0]
            tmp_gene = re.findall(wrk_searchforgene, wrk_pop)
            wrk_gene = tmp_gene[0]
            tmp_rnatype = re.findall(wrk_searchforrnatype, wrk_pop)
            wrk_rnatype = tmp_rnatype[0]
            #print('wrk_acc:', wrk_acc, 'wrk_desc:', wrk_desc, 'wrk_gene', wrk_gene)
            ## Loop through the nucleotides to build a single document
            wrk_data = ''
            for wrk_list in loop1_data:
                wrk_data += wrk_list
            wrk_data_encode = wrk_data.encode()
            fs_forwrite.insert_one({"Taxon":"9606", "Organism":"Homo sapiens", "Acc":wrk_acc, "RNAType":wrk_rnatype, "Gene":wrk_gene, "Description":wrk_desc, 'Nucleotides':wrk_data_encode})
print('End of Genome rna processing...')
