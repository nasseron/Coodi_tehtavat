def main():
    names = set()
    while True:
        name = input('Enter your name: ')
        if name == "":
            break
        if name in names:
            print(name,'Name already taken')
        else:
            names.add(name)
            print(name,"New name aded")
if __name__ == '__main__':
    main()


