yosh = int(input('Yoshingiz nechchida?.'))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')        


yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
else:
    price = 10000

print(f"Sizga kirish {price} so'm")      

yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4: # yosh bolalarga bepul
    price = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh<65: # 12 katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else: # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")   

yosh = int(input('Yoshingiz nechchida?')) 
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 10000
elif yosh<=65:
    price = 8000
print(f"Sizga kirish {price} so'm")



# and, or operatorlari
# or operatori
kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')    


kun = input("Bugun nima kun?>>>") 
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

# and operatori
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani kettik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")

# bir nechta shartlarni ketma-ket yozish

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower())=='shanba' or kun.lower()=='yakshanba') and harorat>=30
    print("Cho'milgani kettik!")
elif (kun.lower())=='shanba' or kun.lower()=='yakshanba') and harorat=30
    print("Uyda dam olamiz!")


narh = 15000 #mijoz 15000 so'mga taom oldi.
choy = True #mijoz choy ham oldi
salat = False #mijoz salat olmadi


if choy and salat: #agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000 #narhga 10000 so'm qo'shamiz
elif choy or salat: #agar choy yoki salat olgan bo'lsa    
narh = narh + 5000 #narhga 5000 qo'shamiz

#shartlarni ketma-ket tekshirish
# ya'ni if-elif-else


narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti False
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy: #agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat: #agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non: # agar non olsa
    print("Mijos non oldi.")
    narh = narh + 2000
if kompot: #agar kompot olsa
    print("Mijos kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijos assorti olsa.")
    narh = narh + 15000
print(f"Jami {narh} so'm")


# Ro'yxat tartibini tekshirish (in OPERATORI)


















