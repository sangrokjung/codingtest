if __name__ == '__main__':
    d = {}
    score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        d[name] = score

    second_lowest_score = sorted(set(score_list))[1]
    result_list = sorted([name for name, score in d.items() if score == second_lowest_score])

    for result in result_list:
        print(result)