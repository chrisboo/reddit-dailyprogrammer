from itertools import product, combinations
from queue import PriorityQueue
from functools import reduce

def all_pairs(lst):
    found_pairs = set()

    pq = PriorityQueue()

    permutations = product(*lst)
    for permutation in permutations:
        pairs = list(combinations(permutation, 2))
        pq.put((-len(pairs), pairs, permutation))

    total_num_pairs = sum([len(a) * len(b) for a, b in combinations(lst, 2)])

    count = 0
    while len(found_pairs) < total_num_pairs:
        length, pairs, permutation = pq.get()
        length = -length
        updated_new_pairs = [pair for pair in pairs if pair not in found_pairs]
        if len(updated_new_pairs) == length:
            print(permutation, updated_new_pairs)
            found_pairs.update(updated_new_pairs)
            count += 1
        else:
            pq.put((-len(updated_new_pairs), updated_new_pairs, permutation))

    print(count)

all_pairs([['0', '1'], ['A', 'B', 'C'], ['D', 'E', 'F', 'G']])
all_pairs([['0', '1', '2', '3'], ['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H', 'I']])
all_pairs([['0', '1', '2', '3', '4'], ['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I'], ['J', 'K', 'L']])