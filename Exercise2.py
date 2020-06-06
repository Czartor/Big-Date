IphoneX = 3000

print('Ile masz pieniędzy?')
money = int(input())
print('Aktualna cena IPhoneX = ', IphoneX)
if IphoneX > money:
    print('Brakuje Ci ', IphoneX - money, 'aby nabyć IPhoneX')
else:
    print('Stać Cię na ', money / IphoneX, 'IPhoneX')
