# egg_drop.py
#
# Solution to the general egg drop problem via:
#
# 1. A recursive-memoized algorithm
# 2. A bottom-up table construction
#
# (C) 2017 J. Arrieta, Nabla Zero Labs
# MIT License.

from time import perf_counter

def egg_drop_recursive_memoized(floors, eggs):

    cache = {}
    num_calls = 0
    num_hits = 0

    def drops(floors, eggs):

        nonlocal cache
        nonlocal num_calls
        nonlocal num_hits

        num_calls += 1

        if floors == 0:
            return 0

        if floors == 1:
            return 1

        if eggs == 1:
            return floors

        key = (floors, eggs)

        if key in cache:
            num_hits += 1
            value = cache[key]
        else:
            value = min(1 + max(drops(floor - 1, eggs - 1),
                                drops(floors - floor, eggs))
                        for floor in range(2, floors + 1))
            cache[key] = value

        return value


    tbeg = perf_counter()
    value = drops(floors, eggs)
    elapsed = (perf_counter() - tbeg) * 1000

    print(f"RECURSIVE MEMOIZED IMPLEMENTATION",
          f"recursive calls........... {num_calls}",
          f"cache hits................ {num_hits}",
          f"cache entries............. {len(cache)}",
          f"number of eggs............ {eggs}",
          f"number of floors.......... {floors}",
          f"minimum number of drops... {value}",
          f"elapsed milliseconds...... {elapsed:.3f}",
          sep="\n", flush=True)

def egg_drop_bottom_up_table(floors, eggs):

    tbeg = perf_counter()

    table = {
        **{(0, e) : 0 for e in range(1, eggs + 1) },
        **{(1, e) : 1 for e in range(1, eggs + 1) },
        **{(f, 1) : f for f in range(1, floors + 1) },
        }

    for egg in range(2, eggs + 1):
        for height in range(2, floors + 1):
            table[height, egg] = min(1 + max(table[floor - 1, egg -1],
                                             table[height - floor, egg])
                                     for floor in range(1, height + 1))

    result = table[floors, eggs]

    elapsed = (perf_counter() - tbeg) * 1000

    print(f"BOTTOM UP TABLE IMPLEMENTATION",
          f"table size............. {len(table)}",
          f"number of eggs......... {eggs}",
          f"number of floors....... {floors}",
          f"minimum drops.......... {result}",
          f"elapsed milliseconds... {elapsed:.3f}",
          sep="\n", flush=True)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("usage: {0} num_floors num_eggs".format(sys.argv[0]))
        sys.exit(1)

    num_floors = int(sys.argv[1])
    num_eggs = int(sys.argv[2])

    egg_drop_recursive_memoized(num_floors, num_eggs)
    egg_drop_bottom_up_table(num_floors, num_eggs)


'''
// TODO:  https://gist.github.com/arrieta/b181bac40829a7f2460c03612b978944
//          https://github.com/Mishco/Egg_problem/tree/master/egg-problem
'''
