print("nama : Achmad fajar fatoni")
print("npm  : 2021020100114")
print ('Berikut adalah barang barang yang ada di toko')

class Malkis():
    def __init__(self, nama, lemak, protein):
        self.nama = nama
        self.lemak = lemak
        self.protein = protein
    def nilai_gizi (self):
        print('nama \t:', self.nama)
        print('lemak \t:', self.lemak) 
        print('protein\t:', self.protein)   
        
jajan1 = Malkis('malkis','2,5g','1g\n')


jajan1.nilai_gizi()

nama = input('masukan jajan apa yang ingin anda beli')

if nama == 'malkis':
    print('harganya cuma 1.000')
elif nama =='roti':
    print('wah lagi habis bosku')
elif nama =='sosis':    
     print('duh habis jugak')     
elif nama =='wafer':
    print('maaf anda yang di cari sedang kosong')     
elif nama =='coklatos':
        print('maaf lagi kosong')     
elif nama =='orio':
        print('maaf lagi habis bro')
elif nama =='biskuat':
        print('maaf jajan yang anda pilih lagi kosong')
elif nama =='kacang koro':
        print('maaf lagi habis bro')
            
    
          
print ('terimakasih')         