def expect(expected, val):
    if expected != val:
        raise Exception('Values are different')

def is_none(obj):
    if obj is not None:
        raise Exception('obj should be None')

def is_arithmetic_sequnce(seq, a1, r):
    if not (seq[0] == a1 and seq[1] == r):
        print(seq)
        raise Exception('incorrect arithmetic sequence')
