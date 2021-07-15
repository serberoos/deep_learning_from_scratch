import XOR
import OR
import NAND
import AND

print("#AND#")
print("1 / 1 =" , AND.and_perceptron(1, 1))
print("0 / 1 =" , AND.and_perceptron(0, 1))
print("1 / 0 =" , AND.and_perceptron(1, 0))
print("0 / 0 =" , AND.and_perceptron(0, 0))

print()

print("#OR#")
print("1 / 1 =" , OR.or_perceptron(1, 1))
print("0 / 1 =" , OR.or_perceptron(0, 1))
print("1 / 0 =" , OR.or_perceptron(1, 0))
print("0 / 0 =" , OR.or_perceptron(0, 0))

print()

print("#NAND#")
print("1 / 1 =" , NAND.nand_perceptron(1, 1))
print("0 / 1 =" , NAND.nand_perceptron(0, 1))
print("1 / 0 =" , NAND.nand_perceptron(1, 0))
print("0 / 0 =" , NAND.nand_perceptron(0, 0))

print()

print("#XOR#")
print("1 / 1 =" , XOR.xor_perceptron(1, 1))
print("1 / 0 =" , XOR.xor_perceptron(0, 1))
print("0 / 1 =" , XOR.xor_perceptron(1, 0))
print("0 / 0 =" , XOR.xor_perceptron(0, 0))
