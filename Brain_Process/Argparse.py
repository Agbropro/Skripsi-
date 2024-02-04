##TUTORIAL ARGPARSE
import argparse

#Parser itu buat nambah argumen sendiri pas nge run kode di shell
parser = argparse.ArgumentParser(description='Calculate the square of a number.')
parser.add_argument('number', type=float, help='The number for which to calculate the square.')
parser.add_argument('--verbose', action='store_true', help='Print additional information.')

#argumen tadi disimpen di args dgn nama tiap argumennya yg di input pertama dlm kolom add_argument (number,--verbose, etc)
args = parser.parse_args()
params = args.number
print(args.number)
#nanti pas ngerun kode di shell pake python Argparse.py terus angka (sesuai tipe data nya yg ditulis di type)