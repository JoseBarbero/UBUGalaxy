import os


# Function to rename multiple files
def rename():
    i = 0
    for directory in ["Forward", "Reverse"]:
        for filename in os.listdir(directory):
            name = filename.split(".")[0]
            extension = filename.split(".")[1:]
            os.rename(directory+"/"+filename, directory+"/"+name.split("_")[0]+"_"+name.split("_")[-2]+"."+".".join(extension))

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    rename()
