import re
def main():
    name="raghvendra sharma"
    match =re.search('sharma',name)
    if match:
        print(match.group(),end='')
    else:
        print("not matched")
if __name__=='__main__':main()