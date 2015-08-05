# coding: utf-8
# Programmet du ska skriva:
# Du har precis startat företag som säljer robotar som du byggt hemma. 
# Du har räknat ut hur mycket du måste sälja dem för för att gå med vinst. 
# Nu saknas bara att summera priset för alla varor och lägga på momsen. 
# Skriv ett program för detta.
# En kund vill köpa: Två robotar (900 kr/st),  en instruktionsbok (100 kr/st)
# När du räknar ut det, kom ihåg att böcker har 6% moms, inte 25%

#robot_price = 900 * 2 * 1.25 + 100 * 1 * 1.06
robot_price = 900
robot_count = 2
robot_vat = 1.25

book_price = 100 
book_count = 1
book_vat = 1.06

print (robot_price * robot_count * robot_vat + book_price * book_count * book_vat)