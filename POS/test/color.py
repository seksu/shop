from colorama import Fore, Back, Style, init
import os

init(autoreset=True)

os.system('cls')

print(Fore.WHITE + Back.RED + Style.BRIGHT + "\t\t\t\t โหมดขาย ")
print(Fore.BLACK + Back.CYAN + Style.NORMAL + ' ลำดับ    รหัสสินค้า                รายการ                   ราคา            จำนวน    ')

for i in range(0,14):
	print("  20\t57010170\tนาย จารุกิตติ์ สุขาติ\t\t\t59\t\t71")

print(Fore.WHITE + Back.RED + Style.BRIGHT + "\t\t\t\t\t\t\t\t  ราคารวม : 915     ")
print(Fore.BLACK + Back.CYAN + Style.NORMAL + ' cm : เพื่อเปลี่ยนโหมด , r : คืนสินค้า , n : เพื่อกรอกจำนวน                             ')
barcode = input("Input : ")