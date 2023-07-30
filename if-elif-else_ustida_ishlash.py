# if-elif-else Ketma Ketligi
# Dastur davomida bir nechta shartni tekshirib talab qilinishi mumkin.
# Bunday holatda biz if-elif-else ketma-ketligidan foydalanamiz.
# elif-else va if so'zlarining jamlanmasi bo'lib,"aks holda, agar..." deb tarjima qilinadi.
# Bunday if bilan boshlanga ketma-ketlig bir nechta elif lardan iborat bo'lishi mumkin.

# Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi,
# birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.


# Diqqat  "if =elif-else" ketma-ketlikda biror shart bajarilishi bilan,
# Python qolgan shartlarni tekshirmaydi.


# Keling bir misol ko'ramiz.Hayvonot bog'iga kirish quyidagicha belgilangan:
# 4 yoshdan kichik bolalarga kirish bepul
# 4 yoshdan 12 yoshgacha kirish 5000 so'm
# 12 yoshdan kattalarga 10000 so'm

# Foydalanuvchidan yoshini so'rab,hayvonot bog'ida kirish chiptasi narhini
# chiqaruvchi dastur yozamiz.
# qani boshladik...

yosh = int(input('Yoshingiz nechchida?'))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

# Yuqoridagi kod avval foydalanuvchi yoshini so'raydi.2-qatorda 4 dan
# kichik ekanligini tekshiradi.Agar bu shart bajarilsa shartlarni tekshirish shu
# yerdayoq to'xtaydi va keyingi shartlar tashlab o'tib ketiladi.

# Sizga kirish bepul.
# Agar yuqoridagi ikki shart ham bajarilmasa,keyingi elif yosh<=12 sharti
# tekshiriladi, agar shart bajarilsa quyidagi natija chiqadi:

# Sizga kirish 5000 so'm

# Agar yuqoridagi ikki shart ham bajarilmasa navbat o'z-o'zidan else bilan
# kelgan kod bajariladi:

# Sizga kirish 10000 so'm

# 'Ko'd yozishda yaxshi amalaiyotlardan biri,kodlarni qisqa yozish va
# buyruqlarni qayta-qayta takrorlamaslik.Bu kelajakda kodni
# o'zgartirishda ham juda qo'l keladigan amaldir...'


yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
else:
    price = 10000
print(f"Sizga kirish {price} so'm")            

# Avval aytganimizdek,  if-elif-else  zanjirda bir nechta elif lar bo'lishi
# mumkin.Misol uchun, hayvonot bog'i qariyalar uchun chegirma e'lon qilsa,
# kodimizni quyidagicha o'zgartirishimiz mumkin:

yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4: # yosh bolalarga bepul
    price = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh<=65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else: # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")    

# if-elif-else zanjirida ham else qismi majburiy emas:

yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 10000
elif yosh<=65:
    price = 8000 
print(f"Sizga kirish {price} so'm")


# AND, OR operatorlari
# Yuqoria aytganimizdek, if-elif-else zanjirda shartlarning biri
# bajarilishi bilan, Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi.
# Lekin ba'zida biz 2 yoki undan ko'p shartlarni tekshirishni talab qilishimiz
# mumkin, buning uchun AND va OR operatorlaridan foydlanamiz.

# OR operatori:
# OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan
# biri bajarilishini tekshirishda ishlatiladi.Quyidagi misolni ko'raylik,
# foydlanuvchidan hafta kunini so'raymiz va agar kun shanba yoki yakshanba
# bo'lsa,bugun dam olish kuni degan xabarni chiqaramiz,aks holda bugun ish kuni degan xabarni chiqaramiz:

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

# 2-qatordagi or operatoriga e'tibor qiling,bu operator
# kun.lower()=='shanba' yoki kun.lower()=='yakshanba'
# shartlaridan biri bajarilsa True qiymatini qataradi

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

# AND opratori:
# AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning
# barchasini bajarilishini tekshirishda ishlatiladi.AND operatori bilan yozilgan
# shartlarning barchasi bajarilgandagina True qiymati qaytadi,agar
# shartlardan biri bajarilmay qolsa ham False qiymati qaytadi.
# Quyidagi misolni ko'ramiz:

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")

# 3-qatordagi and operatori kun.lower()=='yakshanba' va harorat>=30
# shartlarining ikkisi ham bajarilgandagina True qiymatini qaytaradi,
# aks holda qiymat False bo'ladi.
    
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    price("Uyda dam olamiz!")

# Bir nechta shartlarni ketma-ket yozish
# shartlarni yozishda bir nechta "and" va "or" operatorlarini aralashtirib ham
# yozish mumkin.
        
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or ku.lower()=='yakshanba') and harorat<=30:
    print("Uyda dam olamiz!")
# 3-qatorga e'tibor bersangiz avval kun shanba yoki yakshanba ekanligini
# so'ngra haroratni tekshirdik.Bu shart bajarilishi uchun kun shanba yoki
# yakshanba va harorat 30 dan baland bo'lishi shart.    









