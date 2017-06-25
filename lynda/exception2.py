def main():
    try:
        fname="file1.txt"
        if  not fname.endswith(".txt"):
        #    fh=open(fname)
        #else:
            raise ValueError("File should be ended with .txt")
        fh=open(fname)
    except IOError as e:
        print("could not opoened file",e)
    except ValueError as v:
        print(v)
    else:
        print("everything is okay")

if __name__=="__main__":main()