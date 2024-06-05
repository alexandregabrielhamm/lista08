from funcoes import *


pc_carbono = float(input("informe o percentual de carbono de aço: "))
dureza_rockwell = float(input("informe a dureza de rockwell do aço "))
resistencia = float(input("informe a resistencia a pressão do aço"))




grau = calcular_grau(pc_carbono, dureza_rockwell, resistencia)


print ( f" 0 grau do aço: {grau}")