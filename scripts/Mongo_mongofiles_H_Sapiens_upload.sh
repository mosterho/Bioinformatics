#!/bin/bash

cd /run/user/1000/gvfs/smb-share\:server\=dataserver\,share\=datascience/scripts

mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr1.fa put 9606_chromosome1
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr2.fa put 9606_chromosome2
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr3.fa put 9606_chromosome3
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr4.fa put 9606_chromosome4
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr5.fa put 9606_chromosome5
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr6.fa put 9606_chromosome6
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr7.fa put 9606_chromosome7
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr8.fa put 9606_chromosome8
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr9.fa put 9606_chromosome9
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr10.fa put 9606_chromosome10
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr11.fa put 9606_chromosome11
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr12.fa put 9606_chromosome12
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr13.fa put 9606_chromosome13
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr14.fa put 9606_chromosome14
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr15.fa put 9606_chromosome15
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr16.fa put 9606_chromosome16
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr17.fa put 9606_chromosome17
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr18.fa put 9606_chromosome18
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr19.fa put 9606_chromosome19
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr20.fa put 9606_chromosome20
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr21.fa put 9606_chromosome21
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chr22.fa put 9606_chromosome22
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chrMT.fa put 9606_chromosomeMT
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chrUn.fa put 9606_chromosomeUT
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chrX.fa put 9606_chromosomeX
mongofiles --host=mongodb -d=Chromosome -r -l ../NCBIDownload/H_Sapiens_Chromosome/hs_ref_GRCh38.p7_chrY.fa put 9606_chromosomeY
