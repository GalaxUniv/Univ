# VAT = 23%
vat = 0.77
ammount = 15.84
price_wVat = ammount * vat
costOfTheVat = ammount * (1-vat)
print("Ammount {}".format(ammount))
print("VAT 23% {:.2f}".format(costOfTheVat))
print("Ammount wichout vat {:.2f}".format(price_wVat))
