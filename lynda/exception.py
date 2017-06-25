import re
def main():
    try:
        fh = open("xfile1.txt")
    except IOError as e:
        print("Could not open file: ",e)
    else:
        pattern=re.compile("\n")
        for i ,line in enumerate(fh.readlines()):
            match=re.search(pattern,line)
            if match:
                print(i,pattern.sub(".\n",line),end="")
    #else:
        print("done")
if __name__=="__main__":main()