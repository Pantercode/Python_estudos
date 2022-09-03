import locale
locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")
"pt_BR.utf-8"

print('{:n}'.format(5678))
print('{:f}'.format(1579.543))
print('{:n}'.format(1579.543))
print('{:8e}'.format(3.141592653589793))
print('{:8E}'.format(3.141592653589793))
print('{:8g}'.format(3.141592653589793))
print('{:8G}'.format(3.141592653589793))
print('{:5.2%}'.format(3.141592653589793))
