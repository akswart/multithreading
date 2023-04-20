# multithreading

This is a piece of python code intended for multithreaded benchmarking.
It uses a simple division test up to the square root of each number.
Timing is done with time.time() over an average of 10 runs.

This repo is being expanded to include roughly the same multithreaded code in several different languages which are then benchmarked against each other.

Base results with no opt:

All run with end_power = 8

sndd-paar: 735.8

bigiron: 177.8

ironborn: 164.24

laptop: 1263.2

desktop: 103.17
