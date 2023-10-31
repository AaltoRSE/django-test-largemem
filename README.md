# Demo of django app that loads large data only once.

To run:
- install `requirements.txt`
- `gunicorn` in this directory
- Test: `/usr/bin/time -f %e curl http://localhost:8000`

To see the most important lines: `git grep DEMO`

- `largemem/views.py` allocates a large array.
- It also has a view that returns a random value from it.  The view
  waits 5 seconds to simulate computation time (and to verify that
  indpendent requests are being served by different workers)
- gunicorn imports `proj/wsgi.py` at load time thanks to `preload_app=True`
- `proj/wsgi.py` imports `views.py` which allocates the array
- gunicorn does `fork()` to make other processes, which doesn't copy
  memory: Linux does "copy on write" so the large array is only in
  memory once.
- Now, multiple workers can serve requests at the same time, with only
  one copy of the array in memory.

Other notes:
- Nothing here should be special to Django or gunicorn... but the
  web software has to be made in a way that forks all from one process
  and lets you import at the start.
