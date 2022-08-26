import csv, os, argparse

# Renomear csv original para gisaid.csv
# o arquivo deve ser passado na linha de comando
# python3 seq_GisaidToIAM.py -f <arquivo>

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True)
parser.add_argument("--initial", required=True)
parser.add_argument("--final", required=True)
args = parser.parse_args()
new_name = r"gisaid.csv"
os.rename(args.file, new_name)

# TODO: Automatizar a passagem de codInicial e codFinal
# codInicial = "IAM11355"
# codFinal="IAM11544"
codInicial = args.initial
codFinal= args.final
cod_IAM = codInicial
line_count = 0
gisaid_codes = []

with open('gisaid.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=",")
    csv_reader = csv.reader(csv_file, delimiter="\t")
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            string=row[0]
            if string.find(cod_IAM) != -1:
                print(f'{row[1]},{row[0]}')
                gisaid_codes.append([row[1] + "," + row[0]])
                # print(cod_IAM)
                cod_IAM = "IAM" + str(int(cod_IAM[3:]) + 1)
                # print(f"O codigo agora é: {cod_IAM}")
                if string.find(cod_IAM) != -1:
                    print(f'{row[1]},{row[0]}')
                    gisaid_codes.append([row[1] + "," + row[0]])
            elif string.find(cod_IAM) == -1:
                # print(f'{cod_IAM} sem correspondência')
                while string.find(cod_IAM) == -1:
                    cod_IAM = "IAM" + str(int(cod_IAM[3:]) + 1)
                    if string.find(cod_IAM) != -1:
                        print(f'{row[1]},{row[0]}')
                        gisaid_codes.append([row[1] + "," + row[0]])
                    else:
                        print("-" + "," + " ")
                        gisaid_codes.append(["-" + "," + " "])

with open('GisaidToIAM.csv','w') as file:
   for i in gisaid_codes:
        file.writelines(i)
        file.writelines('\n')

print(" ")
print('GisaidToIAM.csv gerado com sucesso')
print(" ")


# print(" ")
# print("========== GISAID CODES ==========")
# print(" ")
# for i in gisaid_codes:
#     print(i)