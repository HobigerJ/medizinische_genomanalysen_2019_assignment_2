#! /usr/bin/env python3

import vcf

__author__ = 'Johanna Hobiger'


class Assignment2:
   
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    

        quality = 0
        counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
            for record in vcf_reader:
                quality = quality + record.QUAL
                counter += 1
                avg_quality = quality / counter
        print("Average quality of the variants is: ", avg_quality)
        return avg_quality
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)        
            for record in vcf_reader:
                counter += 1
        print("Number of variants: ", counter)
        return counter
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        caller_set = set()
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)            
            for record in vcf_reader:
                info = record.INFO["callsetnames"]
                for i in range(len(info)):
                    caller_set.add(info[i])
        print(" Variant caller: ", caller_set)
        return caller_set

        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''

        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                info = record.INFO["difficultregion"] # info ist eine Liste mit 1 eintrag
                reference_version = info[0] # nehme den einen string-eintrag in eine neue string-variable
                print("reference version: ", reference_version[0:4]) 
                break
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_indel:
                    indel_counter += 1
        
        print("Number of INDELs is: ",  indel_counter)
        return indel_counter


    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        snv_counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter += 1
        
        print("Number of SNVs is: ",  snv_counter)
        return snv_counter

        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                counter += record.num_het        
        
        print("Number of heterozygote variants: ", counter)       
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''

        file = open("chr21.vcf") 
        w_f = open("newfile_21_22.vcf", "w+") 
        for line in file:             
            w_f.write(line)
        file.close
        w_f.close

        file = open("chr22.vcf") 
        w_f = open("newfile_21_22.vcf", "a") 
        for line in file: 
            w_f.write(line)
        file.close
        w_f.close

        print("New file with all variants of chr21 and chr22 was created in the current working directory.")
        
        # mit .writer kamen nur errors, die ich nicht beseitigen konnte
    
    def print_summary(self):
        self.get_average_quality_of_file() # 5
        self.get_total_number_of_variants_of_file() # 67784
        self.get_variant_caller_of_vcf() #  {'', 'SolidSE75GATKHC', '10XGATKhaplo', 'HiSeqPE300xfreebayes', 'HiSeqPE300xGATK', 'IonExomeTVC', 'CGnormal', 'SolidPE50x50GATKHC'}
        self.get_human_reference_version()         
        self.get_number_of_indels() # 12774
        self.get_number_of_snvs() # 55 010       
        self.get_number_of_heterozygous_variants() # 56 370      
        self.merge_chrs_into_one_vcf() # geht
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()

    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



