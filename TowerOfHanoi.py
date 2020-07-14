def Tower(a,fro_m,aux,to):
    if a==1:
        print("Move from ",fro_m," To ",to)
        return
    Tower(a-1,fro_m,aux,to)
    print("Move ",a," From ",fro_m," To ",to)
    Tower(a-1,fro_m,aux,to)
a=int(input('Enter number of Disc : '))
Tower(a,'A','C','B')
