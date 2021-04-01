def get_prefix(patterns):
    prefix = [pattern.split('*')[0] for pattern in patterns]
    max_prefix = max(prefix, key=len)
    for pre in prefix:
        if pre != max_prefix[:len(pre)]:
            return None
    return max_prefix

def get_suffix(patterns):
    suffix = [pattern.split('*')[-1] for pattern in patterns]
    max_suffix = max(suffix, key=len)
    for suf in suffix:
        if len(suf) > 0 and suf != max_suffix[-len(suf):]:
            return None
    return max_suffix

def get_middle(pattern):
    text_chunks = pattern.split('*')
    if len(text_chunks) < 3:
        return ''
    else:
        return ''.join(text_chunks[1:-1])
    
def get_answer(patterns):
    prefix = get_prefix(patterns)
    suffix = get_suffix(patterns)
    if prefix is None or suffix is None:
        return '*'
    middle = list(map(get_middle, patterns))
    middle = ''.join(middle)
    return prefix + middle + suffix

tests = int(input())
for x in range(1, tests+1):
    N = int(input())
    patterns = [input() for _ in range(N)]
    ans = get_answer(patterns)
    print("Case #{}: {}".format(x, ans))