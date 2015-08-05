# coding: utf-8
# Programmet du ska skriva:
# Du har precis startat företag som säljer robotar som du byggt hemma. 
# Du har räknat ut hur mycket du måste sälja dem för för att gå med vinst. 
# Nu saknas bara att summera priset för alla varor och lägga på momsen. 
# Skriv ett program för detta.
# En kund vill köpa: Två robotar (900 kr/st),  en instruktionsbok (100 kr/st)
# När du räknar ut det, kom ihåg att böcker har 6% moms, inte 25%

class Product(object):
	def __init__(self, price, count, vat):

		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		return self.price * self.count * self.vat
			
products = [Product(price = 900, count = 2, vat = 1.25), \
Product(price = 100, count = 1, vat = 1.06)] #lista

total_price = products[0].price_with_vat() + products[1].price_with_vat() #ny variabel, där jag sammanställer priset för produkterna. 

print total_price


