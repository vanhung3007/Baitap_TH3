import math
def Nhapbankinh():
    while True:
        try:
            r = int(input("Nhap ban kinh duong tron: "))
        except ValueError:
            print("ban nhap sai du lieu")
            print("ban nen nhap lai du lieu")
        else:
            if(r<0):
                print("Ban kinh duong tron lon hon 0")
                print("Ban nen nhap lai du lieu")
            else:
                break
    return r
#--------------------------------------------------------
def TinhChuVi(R):
    ChuVi=2*R*math.pi
    print("Chu vi hinh tron la: ",Chuvi)
#--------------------------------------------------------
def TinhDienTich(R):
    DienTich=R*RRmath.pi
    print("Dien tich hinh tron la: ",Dientich)
if __name__ == "__main__":
    R=Nhapbankinh()
    TinhChuVi(R)
    TinhDienTich(R)
