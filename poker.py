def straight(ranks):
     if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
         return True
     return False
     
def flush(suits):
     if len(set(suits))==1:
          return True
     return False

def kind(n,ranks):
     for r in ranks:
          if ranks.count(r)==n:
              return r
     return None

def two_pair(ranks):
     highcard=kind(2,ranks)
     locard=kind(2,tuple(reversed(ranks)))

     if highcard!=locard:
         return (highcard, locard)
     return None

def card_ranks(hand):
     ranks=['--23456789TJQKA'.index(r) for r,s in hand]
     ranks.sort(reverse=True)
     return ranks

def card_suits(hand):
    return [s for r,s in hand]

def hand_rank(hand):
    ranks=card_ranks(hand)
    suits=card_suits(hand)

    if straight (ranks) and flush(suits):
        return (8,max(ranks))
    elif kind(4,ranks):
        return (7, kind(4, ranks), kind(1,ranks))
    elif kind (3, ranks) and kind (2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif  flush(suits):
        return (5, max(ranks))
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3,ranks):
        return(3, kind(3,ranks),kind(1,ranks))
    elif two_pair(ranks):
        return(2,kind(2,ranks),rank(2,sorted(ranks)),kind(1,ranks))
    elif kind(2,ranks):
         return (2, kind(2,ranks),kind(1,ranks))
    else:
         return max(ranks)

def poker(hands):
    return  max(hands, key=hand_rank)

hands=[]
line = input("Enter first Hand:\n")
while(line !=''):
    hands.append(tuple(line.split()))
    print("Enter new Hand")
    line=input()
print("Winner is:")
print(poker(hands))

if __name__=="__main__":
      assert(straight([6,5,4,3,2])==True)
      assert(straight([6,5,5,3,2])==False)
      
      
      
