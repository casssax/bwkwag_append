import csv
import sys
import time

def zero_fill(input,length):
    return input.strip().zfill(length)

def write_ag_file(ag_file_name,out_file,zip_list):
    # READ IN AG FILE
    print("open ag file: ", time.time() - start)
    with open(ag_file_name, 'r') as ag_file:
        print("opened ag file: ", time.time() - start)
        print('Writing AG file output...')
        delim_type = ','
        data = csv.reader(ag_file, delimiter=str(delim_type))
        for i in data:
            ag_data = list(i)
            ag_zip = ag_data[9] + ag_data[10]
            #print(ag_zip)
            #ag_zip = zero_fill(ag_data[9],5) + zero_fill(ag_data[10],4)
            #print(ag_zip)
            if ag_zip in zip_list:
                # IF BW KW ZIP9 ON AG FILE, WRITE OUT AG FILE RECORD
                str1 = str(i).replace("\'","\"")
                str2 = str1.replace(" \"","\"")
                out_file.write(str2[1:-1] + "\n")
            else:
                if ag_zip == '0ZIP5ZIP4':
                    # WRITE HEADER RECORD
                    str1 = str(i).replace("\'","\"")
                    str2 = str1.replace(" \"","\"")
                    out_file.write(str2[1:-1] + "\n")
        print("end of job: ",time.time() - start)


def append_agfile(input_file,out_file):
    # READ IN BW KW FILE AND EXTRACT ZIP9 RECORDS
    print("open file: ", time.time() - start)
    data = csv.reader(input_file, delimiter='\t')
    data = [row[4:6] for row in data]
    #print('data: ',data)
    zip_list = []
    print("start loop: ", time.time() - start)
    for csvdata in data:
        listdata = list(csvdata)
        # ZERO FILL ZIP/ZIP4 IF NESSESARY 
        temp_zip = zero_fill(listdata[0],5) + zero_fill(listdata[1],4)
        if temp_zip not in zip_list:
            zip_list.append(temp_zip)
    #print(zip_list)
    print('BW ZIPS LOADED:')
    print("end loop: ", time.time() - start)
    # NAME/PATH OF AG FILE
    ag_file_name = 'C:\\DATA_SAVE\\bwkwag_append\\PD.0365.FP021215OTHER.NEW.OUTPUT.DELIM.TXT'
    # CALL OUTPUT FUNCTION
    input_file.close()
    write_ag_file(ag_file_name,out_file,zip_list)

start = time.time()
fname = 'ANIMAL_PHARMA_05_13_15_IP_KW_CAT_ZIP4_APPEND.txt'
file_ext = '.out'
with open(fname, 'r') as input_file, open(fname + file_ext, 'w') as out_file:
   append_agfile(input_file,out_file)
