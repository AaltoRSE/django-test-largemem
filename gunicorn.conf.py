preload_app = True  # DEMO: this makes it pre-load the django app
workers = 2
wsgi_app = 'proj.wsgi:application'

# Show the amount of memory used before/after each fork.
from resource import getrusage, RUSAGE_SELF
def pre_fork(server, worker):
    print('pre:', getrusage(RUSAGE_SELF).ru_maxrss)
    pass

def post_fork(server, worker):
    print('post:', getrusage(RUSAGE_SELF).ru_maxrss)
    pass
