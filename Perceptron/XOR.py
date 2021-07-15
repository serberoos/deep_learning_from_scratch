import AND
import NAND
import OR

def xor_perceptron(x1, x2):
    s1 = NAND.nand_perceptron(x1, x2)
    s2 = OR.or_perceptron(x1, x2)
    y = AND.and_perceptron(s1, s2)
    return y
