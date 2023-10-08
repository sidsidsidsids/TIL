t = int(input())
for tc in range(1, 1 + t):
    N, M = map(int, input().split())
    papers = list(map(int, input().split()))

    groups = [set([papers[0], papers[1]])]

    for i in range(1, M):

        for group in groups:
            if papers[i*2] in group and papers[i*2+1] in group:
                break
            elif papers[i * 2] in group:
                for ingroup in groups:
                    if papers[i*2+1] in ingroup:
                        group.update(set.union(group,ingroup))
                        groups.remove(ingroup)
                else:
                    group.add(papers[i * 2 + 1])
                break
            elif papers[i * 2 + 1] in group:
                for ingroup in groups:
                    if papers[i*2] in ingroup:
                        group.update(set.union(group, ingroup))
                        groups.remove(ingroup)
                else:
                    group.add(papers[i * 2])
                break
        else:
            groups.append(set([papers[i * 2], papers[i * 2 + 1]]))

    single = N

    print(groups)

    for group in groups:
        single -= len(group)

    answer = single + len(groups)

    print(f'#{tc} {answer}')


