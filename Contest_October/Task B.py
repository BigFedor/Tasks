def argsort(arr, n):
    firlist = [0] * n
    seclist = [0] * n

    for i in range(n):
        firlist[i] = arr[i]
        seclist[i] = i
    for j in range(len(n)):
        for k in range(0, n - j):
            if firlist[k] > firlist[k + 1]:
                firlist[k], firlist[k + 1] = firlist[k + 1], firlist[k]
                seclist[k], seclist[k + 1] = seclist[k + 1], seclist[k]

    return(seclist)

