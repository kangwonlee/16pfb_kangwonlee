f = open("test.scr", 'w')

r = 10

f.write("circle 0.0,0.0 %d" % r)
f.write('\n')

f.write("zoom e")
f.write('\n')

f.close()
