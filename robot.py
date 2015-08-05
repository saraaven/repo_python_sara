# coding: utf-8
# Programmet du ska skriva:
# Du har precis startat företag som säljer robotar som du byggt hemma. 
# Du har räknat ut hur mycket du måste sälja dem för för att gå med vinst. 
# Nu saknas bara att summera priset för alla varor och lägga på momsen. 
# Skriv ett program för detta.
# En kund vill köpa: Två robotar (900 kr/st),  en instruktionsbok (100 kr/st)
# När du räknar ut det, kom ihåg att böcker har 6% moms, inte 25%

class Product(object):

	def price_with_vat(self):
		return self.price * self.count * self.vat

	price = 0
	count = 0
	vat = 0

robot = Product()
robot.price = 900
robot.count = 2
robot.vat = 1.25

book = Product()
book.price = 100
book.count = 1
book.vat = 1.06

print robot.price_with_vat() + book.price_with_vat()


