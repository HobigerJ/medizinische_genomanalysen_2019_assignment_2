#! /usr/bin/env python3

import vcf

__author__ = 'XXX'


class Assignment2:
   
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''    
        '''
        avg_quality = 0
        counter = 0
        GQ_sum = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
            for record in vcf_reader:
                call = record.genotype('HG001')
                counter +=1
                GQ_sum = GQ_sum + call.data[4]
            #    print("counter: ", counter, "sum: ", GQ_sum)
        avg_quality = GQ_sum / counter
        print("Average quality ", avg_quality) '''

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

        # passt
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        counter = 0
        with open("chr22_new.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
        
            for record in vcf_reader:
                call = record.genotype('HG001')
                if call.is_variant:
                    counter += 1
        print("nr of variants: ", counter)

        # gerhard variante
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        caller_set = set()
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)            
            for record in vcf_reader:
                info = record.INFO["callsetnames"]
                for i in range(len(info)):
                    caller_set.add(info[i])
            print(caller_set)


        print("TODO")

        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''

        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            print(vcf_reader.metadata)
        
        # Fragen
        # gibt eigentlich die möglichkeit metadaten["fileDate"], aber referenz gibts nicht als keyword
        # grep: gibt weder ein "genome" noch "reference" in dem file
        
        
    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        indel_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_indel:
                    indel_counter = indel_counter +1
        
        print("Number of INDELS is: ",  indel_counter)
        return indel_counter
        
        # passt

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        snv_counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                if record.is_snp:
                    snv_counter = snv_counter +1
        
        print("Number of Single Nucleotide Variations is: ",  snv_counter)
        return snv_counter

        # passt
        
        
    def get_number_of_heterozygous_variants(self): # "genotype 0/1 means heterozygous A/T"
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            for record in vcf_reader:
                counter += record.num_het        
        
        print("Number of heterozygote variants: ", counter) 
            
        # passt        
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
    

        file = open("chr21_new.vcf") 
        w_f = open("newfile1.vcf", "w+") 
        for line in file: 
            
            w_f.write(line)
        file.close
        w_f.close

        file = open("chr22_new.vcf") 
        w_f = open("newfile1.vcf", "a") 
        for line in file: 
            w_f.write(line)
        file.close
        w_f.close
        
        
    
    def print_summary(self):
        print("Print all results here")
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    #assignment2.get_human_reference_version() # gibt keine referenzangabe in den metadaten
    #assignment2.get_number_of_indels() # 6586
    #assignment2.get_number_of_snvs() # 35 604
    #assignment2.get_number_of_heterozygous_variants() # 29.293
    #assignment2.get_average_quality_of_file() # 625
    #assignment2.merge_chrs_into_one_vcf()
    #assignment2.get_total_number_of_variants_of_file() #42.190
    assignment2.get_variant_caller_of_vcf()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



