
# Target : 270883
# 266052
from collections import Counter

CARDS = [[] for _ in range(7)]

def is_kind(rank_counts, n):
    rank_counts = dict(rank_counts)
    if n in rank_counts.values():
        return True
    if 1 not in rank_counts:
        return False
    nb_j = rank_counts.pop(1)
    if (n - nb_j) not in rank_counts.values():
        return False
    return True

def fill_cards(hand, bid):
    # Count the occurrences of each rank
    rank_counts = Counter(hand)
    # if 5 in rank_counts.values():
    #     CARDS[0].append((hand[0], bid))
    # elif 4 in rank_counts.values():
    #     four = [v for v in rank_counts if rank_counts[v] == 4][0]
    #     one  = [v for v in rank_counts if rank_counts[v] == 1][0]
    #     CARDS[1].append(((four, one), bid))
    # elif 3 in rank_counts.values() and 2 in rank_counts.values():
    #     three = [v for v in rank_counts if rank_counts[v] == 3][0]
    #     two   = [v for v in rank_counts if rank_counts[v] == 2][0]
    #     CARDS[2].append(((three, two), bid))
    # elif 3 in rank_counts.values():
    #     three = [v for v in rank_counts if rank_counts[v] == 3][0]
    #     ones  = tuple(sorted([v for v in rank_counts if rank_counts[v] == 1], reverse=True))
    #     CARDS[3].append(((three, *ones), bid))
    # elif list(rank_counts.values()).count(2) == 2:
    #     twos = tuple(sorted([v for v in rank_counts if rank_counts[v] == 2], reverse=True))
    #     one  = [v for v in rank_counts if rank_counts[v] == 1][0]
    #     CARDS[4].append(((*twos, one), bid))  
    # elif 2 in rank_counts.values():
    #     two = [v for v in rank_counts if rank_counts[v] == 2][0]
    #     ones  = tuple(sorted([v for v in rank_counts if rank_counts[v] == 1], reverse=True))
    #     CARDS[5].append(((two, *ones), bid))
    # else:
    #     CARDS[6].append((tuple(sorted(hand, reverse=True)), bid))
    if is_kind(rank_counts, 5) :
        idx = 6
    elif is_kind(rank_counts, 4):
        idx = 5
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        idx = 4
    elif is_kind(rank_counts, 3):
        is_full = (len(rank_counts) == 3 and 1 in rank_counts)
        idx = 4 if is_full else 3
    elif list(rank_counts.values()).count(2) == 2:
        idx = 2 
    elif is_kind(rank_counts, 2):
        idx = 1
    else:
        idx = 0
    
    CARDS[idx].append((tuple(hand), bid))

  
VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10
}

for i in range(2,10):
    VALUES[str(i)] = i

with open("input.txt", "r") as f:
    for line in f:
        hand, bid = line.split()
        fill_cards([VALUES[card] for card in hand], int(bid))

idx = 1
total = 0
for hand in CARDS:
    h = sorted(hand)
    for player in h:
        print(player[0], player[1])
        total += idx * player[1] 
        idx   += 1  
print(total)
