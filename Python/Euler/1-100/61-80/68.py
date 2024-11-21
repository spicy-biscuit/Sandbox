"""
68: Magic 5-gon Ring
"""

def Permutations(N):
    if N == 1:
        return([[1]])
    if N == 2:
        return([[1, 2], [2, 1]])
    ThisList = Permutations(N - 1)
    Out = []
    Add = N
    for x in ThisList:
        for Index in range(N):
            String = x[:Index] + [Add] + x[Index:]
            Out.append(String)
        # Out.append(x + [Add])
    return(Out)

AllPermutations = Permutations(10)

Out = 0
for Option in AllPermutations:
    First = Option[0] + Option[2] + Option[4]
    Second = Option[1] + Option[4] + Option[7]
    Third = Option[8] + Option[7] + Option[6]
    Fourth = Option[9] + Option[6] + Option[3]
    Fifth = Option[5] + Option[3] + Option[2]

    if First != Second or Second != Third or Third != Fourth or Fourth != Fifth:
        continue

    for x in range(10):
        Option[x] = str(Option[x])

    First = Option[0] + Option[2] + Option[4]
    Second = Option[1] + Option[4] + Option[7]
    Third = Option[8] + Option[7] + Option[6]
    Fourth = Option[9] + Option[6] + Option[3]
    Fifth = Option[5] + Option[3] + Option[2]

    List = [Option[0], Option[1], Option[8], Option[9], Option[5]]
    List = list(map(int, List))

    if Option[0] == str(min(List)):
        String = First + Second + Third + Fourth + Fifth
    if Option[1] == str(min(List)):
        String = Second + Third + Fourth + Fifth + First
    if Option[8] == str(min(List)):
        String = Third + Fourth + Fifth + First + Second
    if Option[9] == str(min(List)):
        String = Fourth + Fifth + First + Second + Third
    if Option[5] == str(min(List)):
        String = Fifth + First + Second + Third + Fourth

    if len(String) == 17:
        continue

    if Out < int(String):
        Out = int(String)

print(Out)