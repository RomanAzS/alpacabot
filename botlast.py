from collections import deque
import itertools

dick = {}

def makelist(channel): # called on joining a channel to make a list
    if channel in dick.keys(): return
    else:
        dick[channel] = []
        dick[channel] = deque(dick[channel], maxlen=51)

def append(channel, user, msg): # called each time a message is recieved (not pm) to add to list
    dick[channel].append("<%s> %s" % (user, msg))
    # if len(dick[channel]) > 51:
        # dick[channel].popleft()
    # else: return

def last(channel, msg): # called on the trigger to pm the user the last messages
    if msg.strip().isdigit():
        n = int(msg.strip())
        if n <= len(dick[channel]):
            return list(itertools.islice(dick[channel], n, None))
        else: return dick[channel] 
    else:
        return dick[channel]