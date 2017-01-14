def toss():
    head_count = 0
    tail_count = 0
    attempts = 0
    for i in range(1, 5001):
        import random
        # x = random.random()
        x_rounded = round(random.random())
        if x_rounded == 1:
            attempts += 1
            head_count += 1
            print "Attempt#{}: Throwing coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far.".format(attempts,head_count,tail_count)
        elif x_rounded == 0:
            attempts += 1;
            tail_count += 1
            print "Attempt#{}: Throwing coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far.".format(attempts,head_count,tail_count)

toss()
