Input = ["""Valve VN has flow rate=0; tunnels lead to valves LW, TK
Valve FQ has flow rate=0; tunnels lead to valves AJ, YC
Valve DO has flow rate=0; tunnels lead to valves RV, HJ
Valve MW has flow rate=0; tunnels lead to valves TE, HJ
Valve LT has flow rate=5; tunnels lead to valves KO, SG, KH, HZ, RV
Valve UJ has flow rate=0; tunnels lead to valves FW, DE
Valve IZ has flow rate=0; tunnels lead to valves LU, SX
Valve FE has flow rate=17; tunnels lead to valves WG, WI, LC
Valve KS has flow rate=25; tunnels lead to valves QA, BT
Valve HJ has flow rate=11; tunnels lead to valves MW, CZ, ZE, DO
Valve WI has flow rate=0; tunnels lead to valves WX, FE
Valve EK has flow rate=0; tunnels lead to valves KE, BS
Valve HD has flow rate=0; tunnels lead to valves KH, FW
Valve HZ has flow rate=0; tunnels lead to valves XY, LT
Valve CD has flow rate=0; tunnels lead to valves XD, LU
Valve OZ has flow rate=0; tunnels lead to valves GX, LW
Valve AA has flow rate=0; tunnels lead to valves EP, FU, DV, OU, HC
Valve OU has flow rate=0; tunnels lead to valves VX, AA
Valve XD has flow rate=10; tunnels lead to valves VX, VW, BS, XY, CD
Valve AI has flow rate=0; tunnels lead to valves KE, FW
Valve GX has flow rate=0; tunnels lead to valves OZ, WX
Valve FW has flow rate=8; tunnels lead to valves AI, FU, UJ, TK, HD
Valve KO has flow rate=0; tunnels lead to valves DV, LT
Valve DV has flow rate=0; tunnels lead to valves KO, AA
Valve CZ has flow rate=0; tunnels lead to valves LU, HJ
Valve WG has flow rate=0; tunnels lead to valves KE, FE
Valve WX has flow rate=15; tunnels lead to valves WI, GX
Valve AJ has flow rate=0; tunnels lead to valves FQ, LU
Valve LC has flow rate=0; tunnels lead to valves LW, FE
Valve XX has flow rate=0; tunnels lead to valves LA, VW
Valve RK has flow rate=0; tunnels lead to valves BX, LW
Valve YC has flow rate=22; tunnels lead to valves FQ, QA
Valve KH has flow rate=0; tunnels lead to valves HD, LT
Valve ZE has flow rate=0; tunnels lead to valves HJ, SX
Valve BX has flow rate=0; tunnels lead to valves KE, RK
Valve VS has flow rate=24; tunnel leads to valve UP
Valve SX has flow rate=16; tunnels lead to valves IZ, ZE, LV
Valve RV has flow rate=0; tunnels lead to valves LT, DO
Valve UP has flow rate=0; tunnels lead to valves VS, LW
Valve EP has flow rate=0; tunnels lead to valves AA, AU
Valve VO has flow rate=0; tunnels lead to valves KE, HC
Valve HC has flow rate=0; tunnels lead to valves AA, VO
Valve TE has flow rate=0; tunnels lead to valves LA, MW
Valve LW has flow rate=19; tunnels lead to valves UP, OZ, LC, VN, RK
Valve SG has flow rate=0; tunnels lead to valves OY, LT
Valve BT has flow rate=0; tunnels lead to valves KS, LU
Valve DE has flow rate=0; tunnels lead to valves LA, UJ
Valve BS has flow rate=0; tunnels lead to valves EK, XD
Valve VX has flow rate=0; tunnels lead to valves OU, XD
Valve TK has flow rate=0; tunnels lead to valves VN, FW
Valve HQ has flow rate=14; tunnel leads to valve LV
Valve LU has flow rate=20; tunnels lead to valves CZ, IZ, AJ, BT, CD
Valve LA has flow rate=7; tunnels lead to valves OY, XX, TE, DE, AU
Valve VW has flow rate=0; tunnels lead to valves XD, XX
Valve LV has flow rate=0; tunnels lead to valves SX, HQ
Valve XY has flow rate=0; tunnels lead to valves XD, HZ
Valve OY has flow rate=0; tunnels lead to valves SG, LA
Valve KE has flow rate=12; tunnels lead to valves VO, EK, WG, AI, BX
Valve AU has flow rate=0; tunnels lead to valves LA, EP
Valve QA has flow rate=0; tunnels lead to valves YC, KS
Valve FU has flow rate=0; tunnels lead to valves AA, FW"""]

# Input = ["""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""]

Input = Input[0].split("\n")

Names = []
FlowRates = []
LeadsTo = []

for x in Input:
  Names.append(x[6:8])
  FlowRates.append(int(x[x.find("=") + 1:x.find(";")]))
  if x.find("valves") != -1:
    x = x[x.find('valves') + 7:]
  else:
    x = x[x.find('to valve') + 9:]
  x = x.split(", ")
  LeadsTo.append(x)

# print(Names)
# print(FlowRates)
# print(LeadsTo)

from functools import cache

@cache
def Paths(Current, Opened, Time):
  # print(Time)
  List = []

  if Time == 1 or Time == 0:
    return(0)

  #Move
  Options = LeadsTo[Names.index(Current)]
  for x in Options:
    List.append(Paths(x, Opened, Time - 1))

  #Open
  if Current not in Opened:
    FlowRate = FlowRates[Names.index(Current)]
    if FlowRate != 0:
      New = Opened + (Current,)
      New = tuple(sorted(New))
      List.append(((Time - 1) * FlowRate) + Paths(Current, New, Time - 1))
  return(max(List))

print(Paths("AA", tuple([]), 30))