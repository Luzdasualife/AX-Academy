def Conversor(hr, min, seg):
    return hr * 3600 + min * 60 + seg

def main():
    h = int(input())
    m = int(input())
    s = int(input())
    
    total = Conversor(h, m, s)
    print("{} segundos".format(total))

if __name__ == "__main__":
    main()