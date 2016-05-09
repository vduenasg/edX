def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

# a = powerSet([1, 2])
# print a.next()
# print a.next()
# print a.next()
# print a.next()

values2 = []
for i in range(8):
    subset = ''
    for j in range(3):
        subset += str((i / (2 ** j)) % 2)
    values2.append(subset)
print values2

values3 = []
for i in range(9):
    subset = ''
    for j in range(2):
        subset += str((i / (3 ** j)) % 3)
    values3.append(subset)
print values3

values4 = []
for i in range(16):
    subset = ''
    for j in range(3):
        subset += str((i / (4 ** j)) % 4)
    values4.append(subset)
print values4
