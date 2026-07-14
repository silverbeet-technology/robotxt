import os
import datetime
import fileinput

file_name = "robots.txt"

site_fqdn = input("Enter your FQDN: ")


with open(file_name, "w") as file:
    file.write("#### robots.txt \n\n")

with open(file_name, 'a') as fout, fileinput.input('src/ua-block-train-block-search.txt') as fin:
    for line in fin:
        fout.write(line)

##### sitemap
with open(file_name) as inputfile, open(file_name, 'a') as outputfile:
        outputfile.write('\n')
with open(file_name, 'a') as fout, fileinput.input('src/sitemap.txt') as fin:
    for line in fin:
        fout.write(line)
with open(file_name, "a") as file:
    file.write("Sitemap: https://" + site_fqdn + "/sitemap.xml\n\n")

##### site-disclaimer 
with open(file_name, 'a') as fout, fileinput.input('src/site-disclaimer.txt') as fin:
    for line in fin:
        fout.write(line)

##### about
with open(file_name) as inputfile, open(file_name, 'a') as outputfile:
        outputfile.write('\n')
with open(file_name, 'a') as fout, fileinput.input('src/about.txt') as fin:
    for line in fin:
        fout.write(line)

##### timestamp
with open(file_name, "a") as file:
    file.write(f"# {file_name} created {datetime.datetime.now()} \n")

##### summary
if os.path.exists(file_name):
    print(f"{file_name} has been created successfully, see file for usage. \n")
