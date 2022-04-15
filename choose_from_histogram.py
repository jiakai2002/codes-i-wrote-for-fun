import random


histogram = {"a": 1, "b": 3, "c": 1}
# the higher the key's frequency, the higher the probability of it geting chosen


def choose_from(histogram):
    new_histogram = []
    for key, value in histogram.items():
        for i in range(0, value):
            new_histogram.append(key)
    print(random.choice(new_histogram))


choose_from(histogram)
