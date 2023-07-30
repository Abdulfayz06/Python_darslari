# Avvalgi darsimizda biz turli ifodalarni solishtirishda TRUE yoki FALSE
# qiymatlari qaytishini ko'rdik.Bu qiymatlar boolean(mantiqiy) qiymatlar deb
# ataladi, va dasturlashda juda keng qo'llaniladi.Pytonda o'zgaruvchilarda
# boolean qiymatlarni ham saqlash mumkin.

# Quyidagi dasturga e'tibor bering.Deylik,restoranimizga kelgan mijoz 15000
# so'mlik taom oldi,biz mijoz qo'shimcha choy va salat ham olgan(olmaganiga)
# qarab ularning narhini ham yakuniy narhga qo;shishimiz kerak.Mijozning choy
# yoki salat olgan(olmaganini) biz TRUE va FALSE qiymatlari bilan belgiladik.
#narh = 15000 #mijoz 15000 so'mga taom oldi.
#choy = True #mijoz choy ham oldi
#salat = False #mijoz salat olmadi 
#if choy and salat: #agar mijoz choy ham salat ham olgan bo'lsa
 #   narh = narh + 10000 #narhga 10000 so'm qo'shamiz
#elif choy or salat: #agar choy yoki salat olgan bo'lsa
  #  narh = narh + 5000 #narhga 5000 so'm qo'shamiz
#print(f"Jami {narh} so'm") #yakuniy narhni chiqaramiz.

# E'tibor bering, choy va salat boolean (mantiqiy) qiymatlar bo'lgani uchun,
# 5 va 7-qatorlarda biz choy==True yoki salat==True deb yozib
# o'tirishimioz shart emas.

# Yuqoeidagi misolda choy = True (choy sotib oldi) va salat = False (salat sotib olmadi) bo'lgani uchun yakuniy narx narh+5000=20000 chiqdi.
# Boolean o'zgaruvchilarni saqlashda TRUE va FALSE qiymatlari o'rniga 1 va 0 sonlarini ham ishlatish mumkin.

# Shartlarni ketma-ket tekshirish
# if-elif-else zanjirining kamchiligidan biri, shartlardan biri bajarilishi
# bilan, qolgan shartlar tekshirilmaydi. Shuning uchun ba'zida shartlarni ketma-ket tekshirish uchun,
# har bir shartni alohida if bilan ajratish talab qilinishi
# mumkin.

# Yuqoridagi misolni kengraytiraylik:

#narh = 15000 #mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy: #agar choy olsa
 #   print("Mijoz choy oldi.")
  #  narh = narh + 3000
#if salat: #agars alat olsa
 #   print("Mijos salat oldi.")
#    narh = narh + 5000    
#if kompot: #agar kompot olsa
 #   print("Mijoz kompot oldi.")
 #   narh = narh + 5000
#if assorti: #agar assorti olsa
 #   print("Mijoz assorti oldi.")
  #  narh = narh + 15000
#print(f"Jami {narh} so'm")

# Ro'yxat tarkibini tekshirish
# in OPERATORI
# in operatori yordamida biz ro'yxatning tarkibida ma'lum bir element borligini
# tekshirishimiz mumkin.
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
'manti' in menu # menu da manti bormi?

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
'osh' in menu #menu da osh bormi?]

menu = ['osh','qozonkabob','shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeymiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunaqa ovqat yo\'q')

# not in OPERATORI    
# not in operatori yordamida esa biror element ro'yxatda yo'qligini
# tekshirishimiz mumkin.

menu = ['osh', 'qozonkabob', 'shashlik','norin', 'somsa']
'manti' not in menu # menu da manti yo'qmi?

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
'osh' not in menu # menu da osh yo'qmi?

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeymiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')

# not operatorini boshqa shartlarning oldidan ham qo'yishimiz
# mumkin.Misol uchun: if not = a==5 ifodasi if a!=5 ifodasi
# bilan bir hil natija qaytaradi.

# yana bir bor takrorlab ko'ramiz:
menu = ['cola', 'fanta', 'pepsi', 'rscola','flesh', 'gorilla']
'redbull' not in menu # menu da redbull yo'qmi?

menu = ['cola', 'fanta', 'pepsi', 'rscola', 'flesh', 'gorilla']
ichimlik = input('Nima ichamiz?>>>')
if ichimlik.lower() not in menu:
    print('Afsuski bizda bunaqa ichimlik yo\'q')
else:
    print('Buyurtma qabul qilindi.')

# ikki ro'yxatni solishtirish
# ikki ro'yxatning tarkibi quyidagicha tekshiriladi:
    
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")  


# Ro'yxat bo'sh emasligini tekshirish

# yuqoridagi dasturimizda biz foydalanuvchi buyurtma berdi deb tasavvur
# qilyapmiz.Lekin foydalanuvchidan bo'sh ro'yxat kelsachi?Demak for tsiklini
# bajarishdan avval ro'yxat bo'sh emasligiga amin bo'lishimiz kerak.Buning
# uchun avvalgi kodimizni quyidagicha o'zgartiramiz:


menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")

# demak if ro'yxat_nomi: ifodasi agar ro'yxatda bir dona element bo'lsa
# ham TRUE qiymat qaytaradi,aks holsa FALSE qiymatini qaytaradi.    








