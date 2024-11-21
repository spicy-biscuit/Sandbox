Input = ["""2056FA18025A00A4F52AB13FAB6CDA779E1B2012DB003301006A35C7D882200C43289F07A5A192D200C1BC011969BA4A485E63D8FE4CC80480C00D500010F8991E23A8803104A3C425967260020E551DC01D98B5FEF33D5C044C0928053296CDAFCB8D4BDAA611F256DE7B945220080244BE59EE7D0A5D0E6545C0268A7126564732552F003194400B10031C00C002819C00B50034400A70039C009401A114009201500C00B00100D00354300254008200609000D39BB5868C01E9A649C5D9C4A8CC6016CC9B4229F3399629A0C3005E797A5040C016A00DD40010B8E508615000213112294749B8D67EC45F63A980233D8BCF1DC44FAC017914993D42C9000282CB9D4A776233B4BF361F2F9F6659CE5764EB9A3E9007ED3B7B6896C0159F9D1EE76B3FFEF4B8FCF3B88019316E51DA181802B400A8CFCC127E60935D7B10078C01F8B50B20E1803D1FA21C6F300661AC678946008C918E002A72A0F27D82DB802B239A63BAEEA9C6395D98A001A9234EA620026D1AE5CA60A900A4B335A4F815C01A800021B1AE2E4441006A0A47686AE01449CB5534929FF567B9587C6A214C6212ACBF53F9A8E7D3CFF0B136FD061401091719BC5330E5474000D887B24162013CC7EDDCDD8E5E77E53AF128B1276D0F980292DA0CD004A7798EEEC672A7A6008C953F8BD7F781ED00395317AF0726E3402100625F3D9CB18B546E2FC9C65D1C20020E4C36460392F7683004A77DB3DB00527B5A85E06F253442014A00010A8F9106108002190B61E4750004262BC7587E801674EB0CCF1025716A054AD47080467A00B864AD2D4B193E92B4B52C64F27BFB05200C165A38DDF8D5A009C9C2463030802879EB55AB8010396069C413005FC01098EDD0A63B742852402B74DF7FDFE8368037700043E2FC2C8CA00087C518990C0C015C00542726C13936392A4633D8F1802532E5801E84FDF34FCA1487D367EF9A7E50A43E90"""]

Input = Input[0]

BinaryInput = ""

def DecimalToBinary(Decimal):
  Bits = -1
  while True:
    Bits += 1
    if Decimal >= 2 ** (Bits):
      continue
    break
  Out = ""
  for x in range(Bits):
    y = Bits - x - 1
    if Decimal >= 2 ** y:
      Decimal -= 2 ** y
      Out = Out + "1"
    else:
      Out = Out + "0"
  return(Out)

def BinaryToDecimal(Binary):
  Bits = len(Binary)
  Out = 0
  for x in range(Bits):
    y = Bits - x - 1
    if Binary[x] == "1":
      Out += 2 ** (y)
  return(Out)

def HexToBinary(String):
  Out = ""
  for x in range(len(String)):
    Now = String[x]
    Value = 0
    if Now.isdigit():
      Value = int(Now)
    else:
      Value = ord(Now) - 65 + 10
    Value = DecimalToBinary(Value)
    while True:
      if len(Value) == 4:
        break
      Value = "0" + Value
    Out = Out + Value
  return(Out)

def DecodePacket(Packet):
  # if len(Packet) <= 6:
  #   return([])
  # print(Packet)
  PacketVersion = BinaryToDecimal(Packet[:3])
  Packet = Packet[3:]
  TypeID = BinaryToDecimal(Packet[:3])
  Packet = Packet[3:]
  # print(PacketVersion, TypeID)

  if TypeID == 4:
    Out = ""
    while True:
      ThisPart = Packet[:5]
      Packet = Packet[5:]
      Prefix = int(ThisPart[0])
      ThisPart = ThisPart[1:]
      Out = Out + ThisPart
      if Prefix == 0:
        Out = BinaryToDecimal(Out)
        return([PacketVersion, Packet])

  LengthTypeID = int(Packet[0])
  Packet = Packet[1:]

  if LengthTypeID == 0:
    TotalLength = BinaryToDecimal(Packet[:15])
    Packet = Packet[15:]
    Analyze = Packet[:TotalLength]
    Packet = Packet[TotalLength:]
    # List = []
    # List = [PacketVersion] + DecodePacket(Analyze)
    # return(List)
    List = [PacketVersion]
    while True:
      Output = DecodePacket(Analyze)
      List.append(Output[0])
      Analyze = Output[1]
      if len(Analyze) <= 6:
        return([sum(List), Packet])
    
    # return([PacketVersion, Packet])

  if LengthTypeID == 1:
    TotalPackets = BinaryToDecimal(Packet[:11])
    Packet = Packet[11:]
    Analyze = Packet
    List = [PacketVersion]
    for x in range(TotalPackets):
      Output = DecodePacket(Packet)
      List.append(Output[0])
      Packet = Output[1]
    return([sum(List), Packet])
  

x = Input
x = HexToBinary(x)
print(DecodePacket(x)[0])