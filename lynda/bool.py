def main():
    t=True
    print(id(t))
    t=False
    print(id(t))
    x=True
    print(id(x))
    t=True
    print(id(t))


if __name__=="__main__":main()