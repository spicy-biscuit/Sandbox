Input = ["""Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"""]

# Input = ["""e => H
# e => O
# H => HO
# H => OH
# O => HH

# HOHOHO"""]

from functools import cache

Input = Input[0].split("\n\n")

Conversions = Input[0]
OriginalThing = Input[1]

Conversions = Conversions.split("\n")
for Index in range(len(Conversions)):
  Conversion = Conversions[Index]
  Conversion = Conversion.split()
  Conversion = [Conversion[0], Conversion[2]]
  Conversions[Index] = Conversion

def PossibleConversions(OriginalMolecule):
  AllMolecules = []
  for Conversion in Conversions:
    for Index in range(len(OriginalMolecule) - len(Conversion[0]) + 1):
      Length = len(Conversion[0])
      Current = OriginalMolecule[Index:Index + Length]
      if Current == Conversion[0]:
        NewMolecule = OriginalMolecule[:Index] + Conversion[1] + OriginalMolecule[Index + Length:]
        AllMolecules.append(NewMolecule)
  return(list(set(AllMolecules)))

@cache
def ReversePossibleConversions(OriginalMolecule):
  AllMolecules = []
  for Conversion in Conversions:
    for Index in range(len(OriginalMolecule) - len(Conversion[1]) + 1):
      Length = len(Conversion[1])
      Current = OriginalMolecule[Index:Index + Length]
      if Current == Conversion[1]:
        NewMolecule = OriginalMolecule[:Index] + Conversion[0] + OriginalMolecule[Index + Length:]
        AllMolecules.append(NewMolecule)
  return(list(set(AllMolecules)))

def ReverseOneConversion(OriginalMolecule):
  AllMolecules = []
  Breakout = False
  for Conversion in Conversions:
    for Index in range(len(OriginalMolecule) - len(Conversion[1]) + 1):
      Length = len(Conversion[1])
      Current = OriginalMolecule[Index:Index + Length]
      if Current == Conversion[1]:
        NewMolecule = OriginalMolecule[:Index] + Conversion[0] + OriginalMolecule[Index + Length:]
        AllMolecules.append(NewMolecule)
        Breakout = True
        break
    if Breakout:
      break
  return(list(set(AllMolecules)))

CurrentMolecules = [OriginalThing]
SecondList = []




Steps = 0
while True:
  Steps += 1
  for Molecule in CurrentMolecules:
    SecondList = SecondList + ReversePossibleConversions(Molecule)
  
  CurrentMolecules = []
  Breakout = False
  for Molecule in SecondList:
    if Molecule == "e":
      Breakout = True
      break
    if Molecule.find("e") == -1:
      CurrentMolecules.append(Molecule)
  if Breakout:
    break
  SecondList = []
  CurrentMolecules = list(set(CurrentMolecules))
  
  # print(CurrentMolecules)
  print(Steps)
  print(len(CurrentMolecules))

print(Steps)


