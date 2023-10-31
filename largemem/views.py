import random
import resource
import time

from django.http import HttpResponse

# Create your views here.


# DEMO: Load a large array into memory
import numpy as np
N = 1_000_000_000  # bytes
largearray = np.random.randint(2**8, size=(N, ), dtype=np.uint8)


def index(request):
    """Return a random value from the large array.

    Wait some time to simulate processing.
"""
    n = random.randint(0, N)
    resources = resource.getrusage(resource.RUSAGE_SELF)
    time.sleep(5)
    return HttpResponse(f"{n} is {largearray[n]}.\nMem: {resources.ru_maxrss}, {resources.ru_ixrss}, {resources.ru_idrss}, {resources.ru_isrss}\n")
