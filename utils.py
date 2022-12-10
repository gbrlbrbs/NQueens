import itertools
import numpy as np


def is_non_attacking(pair: tuple[int], state: list[int]) -> bool:
    i, j = pair
    if state[i] == state[j]:
        return False
    difcol = abs(i - j)
    difrow = abs(state[i] - state[j])
    return difcol != difrow


def fitness(state: list[int]) -> int:
    idx_list = [i for i, _ in enumerate(state)]
    pairs = list(itertools.combinations(idx_list, 2))
    score_arr = np.array(list(map(lambda x: is_non_attacking(x, state), pairs)), dtype=np.bool8).astype(np.int32)
    score: int = score_arr.sum()
    return score