if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    scores = list(set(scores))
    scores.sort(reverse=True)

    print(scores[1])