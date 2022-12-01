#!/usr/bin/python3
if __name__ == "__main__":
    import hidded_4

    names = dir(hidded_4)
    for name in names:
        if name[:2] == "__":
            continue
        print(name)
