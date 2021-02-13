def count_answers(raw):
    raw = sorted(raw)
    raw = list(dict.fromkeys(raw))
    if '\n' in raw:
        raw.remove('\n')
    return len(raw)


def count_answers_strict(raw):
    ans = raw.split('\n')
    if '' in ans:
        ans.remove('')

    if len(ans) == 1:
        return len(ans[0])

    res = 0
    first = ans[0]
    for c in first:
        contains = 1
        for an in ans[1:]:
            if c not in an:
                contains = 0
                break
        res = res + contains

    return res


def char_in_answers(c, ans):
    if len(ans) == 1:
        if c in ans[0]:
            return 1
        else:
            return 0
    else:
        an = ans[0]
        if c in an:
            return


def main():
    answers = open('./input', 'r').read().split('\n\n')
    ans_count = 0
    strict_count = 0
    for ans in answers:
        ans_count = ans_count + count_answers(ans)
        strict_count = strict_count + count_answers_strict(ans)
    print('Number of answers to part 1: ' + str(ans_count))
    print('Number of answers to part 2: ' + str(strict_count))

    return


if __name__ == '__main__':
    main()
