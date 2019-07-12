import os
import pandas as pd

abricate_files = []

# Working directory selection
# If there is only one directory, it is selected. If there are more, the user selects it.
results_folders = [f for f in os.listdir(".") if f.startswith("Results") and "." not in f]

if len(results_folders) > 1:
    folders_dict = dict(zip(range(len(results_folders)), results_folders))
    print("Select which folder you want to work in: (type just the number on the left)")
    for key, value in folders_dict.items():
        print("\t( "+str(key)+" ) : "+value)
    selected = input()
    while selected not in range(len(results_folders)):
        print("You have to introduce a number from the list.")
        selected = input()
    working_dir = folders_dict[selected]
elif len(results_folders) == 1:
    working_dir = results_folders[0]
else:
    print("At least one results folder started by \"Results\" must exist.")


for file_name in os.listdir(working_dir+"/roary"):
    if file_name.endswith(".csv"):
        roary = pd.read_csv("./"+working_dir+"/roary/"+file_name)


for file_name in os.listdir(working_dir+"/abricate"):
    abricate_files.append(pd.read_csv(working_dir+"/abricate/"+file_name, sep="\t"))
abricate = pd.concat(abricate_files)

i = 1
while working_dir+".xlsx" in os.listdir("."):
    i += 1
    working_dir = working_dir.split("__")[0] + "__" + str(i)

writer = pd.ExcelWriter(working_dir+".xlsx")

abricate.to_excel(writer, 'ABRicate')
roary.to_excel(writer, 'Roary')

writer.save()

print(working_dir+".xlsx has been created.")
