import os
import sys

# Function to rename multiple files
def rename():
	if len(sys.argv) > 1:
		if sys.argv[1] == "help":
			print("Usage: \n Write \t renamefastq *directory path* \t and every fastq file in this directory will be renamed.")
			print("Example: \n renamefastq ./Forward \t will rename every file in Forward directory")
		else:
			for filename in os.listdir(sys.argv[1]):
				name = filename.split(".")[0]
				extension = filename.split(".")[1:]
				os.rename(sys.argv[1]+"/"+filename, sys.argv[1]+"/"+name.split("_")[0]+"_"+name.split("_")[-2]+"."+".".join(extension))
	else:
		print("You need to provide a directory route.")

if __name__ == '__main__':
	rename()
