# -*- coding: UTF-8 -*-
#포커 게임

from copy import deepcopy

NB = 0 #넘버
PT = 1 #패턴

#스트레이트용 숫자 배치
STNUM = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'T':10, 'J':11, 'Q':12, 'K':13, 'A':1}
#HIGH용 숫자 순위
NUM = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
       'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
#패턴 순위
PAT = {'C':1, 'D':2, 'H':3, 'S':4}
#족보 순위
SET = {'X':1, 'OP':2, 'TP':3, 'TK':4, 'ST':5, 'FL':6, 'FH':7, 'FK':8, 'SF':9, 'RF':10}
SETSTR = {'X':'High Card', 'OP':'One Pair', 'TP':'Two Pairs',
          'TK':'Three of a Kind', 'ST':'Straight', 'FL':'Flush',
          'FH':'Full House', 'FK':'Four of a Kind',
          'SF':'Straight Flush', 'RF':'Royal Flush'}

#두 리스트가 같은 조합인지 확인
#입력: 리스트 2개
def isSame(P1, P2):
    #원본 손상 방지
    C1 = deepcopy(P1)
    C2 = deepcopy(P2)
    C1.sort()
    C2.sort()
    return (C1 == C2)

#STNUM을 이용하여 스트레이트 확인
#입력: 카드 넘버 리스트
def isStraight(N):
    N = [int(STNUM[x]) for x in N]
    N.sort()
    for i in range(0,5-1):
        if not N[i+1]-N[i] == 1: return False
    return True

#조합이 10, J, Q, K, A 인지 확인
#입력: 카드 패턴 리스트
def isRoyal(P):
    return isSame(P, ['T', 'J', 'Q', 'K', 'A'])

#카드 패턴이 몇 개나 일치하는지 Chunk크기 리스트로 반환
#입력: 패턴 리스트
def getSameNum(P):
    C = deepcopy(P)
    C.sort()
    c = 1
    a = []
    for i in range(0,5-1):
        if not C[i+1] == C[i]:
            a.append(c)
            c = 1
            continue
        c += 1
    a.append(c)
    return a

#가장 높은 순위 카드를 (NUM, PAT)순위형태로 반환
#입력: 카드 리스트
def getHigh(cards):
    #일단 Chunk를 얻기 위해 카드를 숫자 배열로 하여 정렬
    C = [(NUM[cards[i][NB]],PAT[cards[i][PT]]) for i in range(0,5)]
    C.sort()

    c = 1
    a = []
    #Chunk를 얻되 어떤 숫자의 Chunk인지 저장
    for i in range(0,5-1):
        if not C[i+1][0] == C[i][0]:
            a.append((c,C[i][0]))
            c = 1
            continue
        c += 1
    a.append((c,C[-1][0]))
    
    #가장 큰 Chunk의 숫자를 얻는다 Chunk 크기가 같으면
    #자동으로 높은 숫자가 선택됨
    highNum = max(a)[1]

    #원래 카드 배열에서 highNum에 해당하는 애들만 추림
    return max([x for x in C if x[0] == highNum])

#포커 족보 반환
#입력: 카드 리스트
def getSet(cards):
    N = [x[NB] for x in cards]
    P = [x[PT] for x in cards]

    numChunk = getSameNum(N)
    patChunk = getSameNum(P)

    ST = isStraight(N)
    FL = isSame(patChunk, [5])
    R = isRoyal(P)
    
    SET = ''
    if R and FL: SET = 'RF'
    elif ST and FL: SET = 'SF'
    elif isSame(numChunk, [1,4]): SET = 'FK'
    elif isSame(numChunk, [2,3]): SET = 'FH'
    elif FL: SET = 'FL'
    elif ST: SET = 'ST'
    elif isSame(numChunk, [1,1,3]): SET = 'TK'
    elif isSame(numChunk, [1,2,2]): SET = 'TP'
    elif isSame(numChunk, [1,1,1,2]): SET = 'OP'
    else: SET = 'X'

    HIGH = getHigh(cards)

    return [SET, HIGH]

#어느쪽이 이겼는지 알려줌 C1->1 C2->2
#입력: 카드 리스트 2개
def whoWin(C1, C2):
    G1 = getSet(C1)
    G2 = getSet(C2)

    #족보에서 갈린경우
    if SET[G1[0]] > SET[G2[0]]: return 1
    elif SET[G1[0]] < SET[G2[0]]: return 2

    #족보가 같은경우
    if G1[1] > G2[1]: return 1
    elif G1[1] < G2[1]: return 2
    return 0
    
#카드 정보 출력
#입력: 카드 리스트
def printInfo(cards):
    N = [x[NB] for x in cards]
    P = [x[PT] for x in cards]
    numChunk = getSameNum(N)
    patChunk = getSameNum(P)
    SET = getSet(cards)
    
    print "Cards:\t\t", cards
    print "Number:\t\t", N
    print "Pattern:\t", P
    print "numChunk:\t", numChunk
    print "patChunk:\t", patChunk
    print "Set:\t\t", SET[0], SETSTR[SET[0]]
    print "High:\t\t", SET[1]
    print ""

def printInfo2(C1, C2):
    print "[PLAY]"
    printInfo(C1)
    printInfo(C2)
    print "Winner:\t", whoWin(C1,C2)
    print "\n"

def main():
    lines = []
    f = open("poker.txt", 'r')
    while True:
        line = f.readline()
        if not line: break;
        lines.append(line[0:-1].split())
    f.close()

    cnt = 0
    for i in range(len(lines)):        
        C1 = lines[i][0:5]
        C2 = lines[i][5:len(lines[i])]
        printInfo2(C1, C2)
        if whoWin(C1,C2) == 1: cnt += 1
    print cnt

if __name__ == "__main__":
    main()
    pass
