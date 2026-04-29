'''
Benchmarking for searching algorithms.
'''

from searching import linear_search, binary_search


SEARCH_LIST = list(range(100000))
TARGET = -1


def benchmark_search(option):
    option(SEARCH_LIST, TARGET)


def test_linear_search_benchmark(benchmark):
    benchmark.pedantic(
        benchmark_search,
        args=(linear_search,),
        rounds=5,
        iterations=5
    )