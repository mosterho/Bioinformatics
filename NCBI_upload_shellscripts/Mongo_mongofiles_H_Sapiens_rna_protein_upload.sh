#!/bin/bash

##cd /run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/scripts

mongofiles --host=mongodb -d=rna -r -l /run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/NCBIDownload/H_Sapiens_Chromosome/rna.fa put rna
mongofiles --host=mongodb -d=protein -r -l /run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/NCBIDownload/H_Sapiens_Chromosome/protein.fa put protein
