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
        print("Average quality ", avg_quality)
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        counter = 0
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
        
            for record in vcf_reader:
                call = record.genotype('HG001')
                if call.is_variant:
                    counter += 1
        print("nr of variants: ", counter)
    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        print("TODO")
        
        # ? was soll da rauskommen?
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''

        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh)
            print(vcf_reader.metadata)
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
        
        # gleiche formel wie bei snv zählen

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

        # sollte richtig sein, ist von ihm
        
        
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
            
        # num_het nimmt "number of heterozygous genotypes". sollte passen      
        
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        with open("chr22.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
            vcf_writer = vcf.Writer(open("outputfile.vcf", "a+"), vcf_reader)

            for record in vcf_reader:
                call = record.genotype('HG001')
                if call.is_variant:
                    vcf_writer.write_record(record)
        '''
        with open("chr21.vcf") as my_vcf_fh:
            vcf_reader = vcf.Reader(my_vcf_fh) 
            vcf_writer = vcf.Writer(open("outputfile.vcf", "a+"), vcf_reader)

            for record in vcf_reader:
                call = record.genotype('HG001')
                if call.is_variant:
                    vcf_writer.write_record(record) ''' # das geht nicht weil wir keinen sample namen für chr21 haben


        #print("TODO")
        
        #print("Number of total variants")

        # gibt KEIN 0|0 zuück, müsste also passen
        
    
    def print_summary(self):
        print("Print all results here")
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2()
    assignment2.print_summary()
    # assignment2.get_human_reference_version() # gibt keine referenzangabe in den metadaten
    #assignment2.get_number_of_indels() # 6586
    #assignment2.get_number_of_snvs() # 35 604
    #assignment2.get_number_of_heterozygous_variants() # 29.293
    #assignment2.get_average_quality_of_file() # 625
    #assignment2.merge_chrs_into_one_vcf()
    assignment2.get_total_number_of_variants_of_file() #42.190
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



