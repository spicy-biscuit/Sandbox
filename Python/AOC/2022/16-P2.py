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

Input = ["""Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""]

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

Usefuls = ["AA"]
for x in Names:
  Flow = FlowRates[Names.index(x)]
  if Flow != 0:
    Usefuls.append(x)

# print(Usefuls)

Grid = [[0 for x in range(len(Usefuls))] for x in range(len(Usefuls))]

from functools import cache

@cache
def MinDistance(Start, End, Length):
  if Start == End:
    return(Length)
  if Length >= len(Names) + 20:
    return(float('inf'))
  This = []
  for x in LeadsTo[Names.index(Start)]:
    This.append(MinDistance(x, End, Length + 1))
  return(min(This))

for X in Usefuls:
  for Y in Usefuls:
    if X == Y:
      continue
    Grid[Usefuls.index(X)][Usefuls.index(Y)] = MinDistance(X, Y, 0)

for x in Grid:
  print(x)

# @cache
# def OldPaths(You, Opened, Time):
#   if Time == 0 or Time == 1:
#     return(0)

#   YouTimeLeft = You[1]
#   YouPosition = You[0]

#   #Continue on path
#   if YouTimeLeft != 0:
#     YouTimeLeft -= 1
#     NewYou = (YouPosition, YouTimeLeft)
#     return(Paths(NewYou, Opened, Time - 1))

#   if YouTimeLeft == 0:
#     List = [0]
#     #Open
#     if YouPosition not in Opened:
#       if YouPosition != "AA":
#         New = Opened + (YouPosition,)
#         New = tuple(sorted(New))
#         List.append((Time - 1) * FlowRates[Names.index(YouPosition)] + Paths(You, New, Time - 1))
  
#     #Move
#     for NewPosition in Usefuls:
#       if NewPosition == "AA":
#         continue
#       if NewPosition in Opened:
#         continue
#       NewDistance = Grid[Usefuls.index(NewPosition)][Usefuls.index(YouPosition)]
#       List.append(Paths((NewPosition, NewDistance - 1), Opened, Time - 1))
#     return(max(List))

@cache
def Paths(You, Elephant, Opened, Time):
  if Time == 0 or Time == 1:
    return(0)

  YouTimeLeft = You[1]
  YouPosition = You[0]
  ElephantTimeLeft = Elephant[1]
  ElephantPosition = Elephant[0]

  #Continue on path
  if YouTimeLeft != 0 and ElephantTimeLeft != 0:
    YouTimeLeft -= 1
    ElephantTimeLeft -= 1
    NewYou = (YouPosition, YouTimeLeft)
    NewElephant = (ElephantPosition, ElephantTimeLeft)
    return(Paths(NewYou, NewElephant, Opened, Time - 1))

  if YouTimeLeft == 0 and ElephantTimeLeft != 0:
    #ELEPHANT CONTINUES, YOU CHANGE
    List = [0]
    ElephantTimeLeft -= 1
    NewElephant = (ElephantPosition, ElephantTimeLeft)
    #Open
    if YouPosition not in Opened:
      if YouPosition != "AA":
        New = Opened + (YouPosition,)
        New = tuple(sorted(New))
        List.append((Time - 1) * FlowRates[Names.index(YouPosition)] + Paths(You, New, NewElephant, Time - 1))
  
    #Move
    for NewPosition in Usefuls:
      if NewPosition == "AA":
        continue
      if NewPosition in Opened:
        continue
      NewDistance = Grid[Usefuls.index(NewPosition)][Usefuls.index(YouPosition)]
      List.append(Paths((NewPosition, NewDistance - 1), NewElephant, Opened, Time - 1))
    return(max(List))

  if ElephantTimeLeft == 0 and YouTimeLeft != 0:
    #YOU CONTINUE, ELEPHANT CHANGES
    List = [0]
    YouTimeLeft -= 1
    NewYou = (YouPosition, YouTimeLeft)
    #Open
    if ElephantPosition not in Opened:
      if ElephantPosition != "AA":
        New = Opened + (ElephantPosition,)
        New = tuple(sorted(New))
        List.append((Time - 1) * FlowRates[Names.index(ElephantPosition)] + Paths(You, NewYou, New, Time - 1))
  
    #Move
    for NewPosition in Usefuls:
      if NewPosition == "AA":
        continue
      if NewPosition in Opened:
        continue
      NewDistance = Grid[Usefuls.index(NewPosition)][Usefuls.index(ElephantPosition)]
      List.append(Paths(NewYou, (NewPosition, NewDistance - 1), Opened, Time - 1))
    return(max(List))

  if ElephantTimeLeft != 0 and YouTimeLeft != 0:
    List = []

    #You move, Elephant opens
    

    #You open, elephant moves


    #Both open


    #Both move



print(Paths(("AA", 0), tuple([]), 30))