################################################################################
# 08/01/2016
#
# Abderrahmen Hadjadj-Aoul
# Gabriel Greslin
#
# SD314: Miniproject – FP in Python
#
################################################################################

################################################################################
# 1.
# write a function loop such that loop(p, f, x) returns
# x when p(x) is True and
# loop(p, f, x) returns loop(p, f, f(x)) otherwise.
loop = lambda p, f, x: x if p(x) else loop(p, f, f(x))

# Tests
print("# loop(p, f, x) - TESTS")
print("#######################\n")

# Test 1
print("# loop(p, f, x) - Test 1")
p = lambda x: not x < 5
def f(x):
    print("x:"+str(x))
    return x+1
y = loop(p, f, 1)
print("*y:"+str(y))
print("")

################################################################################
# 2.
# write a function exists such that exists(p, l) returns
# True when there is an element of list l such that p(l) is true.
exists = lambda p, l: p(l[0]) or exists(p, l[1:]) if len(l) > 0 else False

# Tests
print("# exists(p, l) - TESTS")
print("######################\n")

# Test 1
print("# exists(p, l) - Test 1")
l = [1,2,3,4,5]
p = lambda x: x == 2
r = exists(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:True")
if r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# exists(p, l) - Test 2")
l = [1,3,4,5]
p = lambda x: x == 2
r = exists(p, l)
print("l")
print(l)
print("r:"+str(r))
if not r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 3
print("# exists(p, l) - Test 3")
l = [1,3,4,5]
p = lambda x: x > 5
r = exists(p, l)
print("l")
print(l)
print("r:"+str(r))
if not r:
    print("test:passed")
else:
    print("test:ERROR")
print("")

################################################################################
# 3.
# write a function find such that find(p, l) returns
# x if x is the first element of l such that p(x) is True.
# When no such element exists, simply return None.
find  = lambda p, l: ( l[0] if p(l[0]) else find(p, l[1:]) ) if len(l) > 0 else None

# Tests
print("# find(p, l) - TESTS")
print("#####################\n")

# Test 1
print("# find(p, l) - Test 1")
l = [1,2,3,4,5]
p = lambda x: x == 3
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:3")
if r == 3:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# find(p, l) - Test 1")
l = [1,2,3,4,5, 7, 8, 9]
p = lambda x: x > 5
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:7")
if r == 7:
    print("test:passed")
else:
    print("test:ERROR")
print("")

# Test 2
print("# find(p, l) - Test 1")
l = [1,2,3,4,5, 7, 8, 9]
p = lambda x: x == 6
r = find(p, l)
print("l")
print(l)
print("result:"+str(r))
print("expected:None")
if r == None:
    print("test:passed")
else:
    print("test:ERROR")
print("")
