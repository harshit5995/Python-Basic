if __name__ == '__main__':
    n = int(input())
    student_marks = dict()
    scores =list()
    marks = list()
    sum = float()
    for _ in range(n):
        word = input().split()
        name = word[0]
        m1 = float(word[1])
        m2 = float(word[2])
        m3 = float(word[3])
        scores.append([m1,m2,m3])
        student_marks[name] = scores[_]

    query_name = input()

    marks = student_marks[query_name]
    for j in marks:
        sum += float(j)
        ap = sum /3
    print("%.2f"%(ap))