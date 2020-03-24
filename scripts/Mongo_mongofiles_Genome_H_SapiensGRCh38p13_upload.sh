#!/bin/bash

##cd /run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience

mongofiles --host=mongodb -d=Genome  -r -l=/run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/NCBIDownload/Genome/homoSapiens/GCF_000001405.39_GRCh38.p13_genomic.fna put 9606_Genome
mongofiles --host=mongodb -d=Genome  -r -l=/run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/NCBIDownload/Genome/homoSapiens/GCF_000001405.39_GRCh38.p13_rna.fna put 9606_Genome_rna
mongofiles --host=mongodb -d=Genome  -r -l=/run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/NCBIDownload/Genome/homoSapiens/GCF_000001405.39_GRCh38.p13_protein.faa put 9606_Genome_protein
