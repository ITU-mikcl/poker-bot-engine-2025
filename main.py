import sys
from example_bots.python import random_bot, never_bluff_bot, chicken_bot
from test import run_benchmark, run_table
import my_bot
import javabot.java_wrapper as java_wrapper

bots = [random_bot, never_bluff_bot, chicken_bot]

lang, type = sys.argv[1], sys.argv[2]

if lang == "java":
    bots.append(java_wrapper)
else:
    bots.append(my_bot)

if type == "benchmark":
    run_benchmark(bots, int(sys.argv[3]))
else:
    run_table(bots)
