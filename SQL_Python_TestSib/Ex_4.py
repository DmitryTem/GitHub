

def long_repeat(line):
    """length the longest substring that consists of the same char """
    result = 0
    n = 1
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            n = n + 1
        else:
            n = 1

        if n > 1 and n > result:
            result = n

    return result


if __name__ == '__main__':
    #autotests
    assert long_repeat('sdsffffse') == 4, "First" 
    assert long_repeat('ddvvrwwwrggg') == 3, "Second" 
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, ":("
    print('Looks good')