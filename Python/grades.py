def grades():
    for x in range(1,11):
        i = input()
        if i > 100:
            print "Score: {}; Stop it, stop it, you're lying!".format(i)
        if i >= 90:
            print "Score: {}; Your grade is A".format(i)
        elif i >= 80:
            print "Score: {}; Your grade is B".format(i)
        elif i >= 70:
            print "Score: {}; Your grade is C".format(i)
        elif i >= 60:
            print "Score: {}; Your grade is D".format(i)
        else:
            print "Score: {}; You fail".format(i)


grades()
