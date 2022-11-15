
#input generator
def generation(filename):
    f = open(filename,"r")
    letter1,num1,letter2,num2 = "",[],"",[]
    for line in f:
        info = line.split("\n")[0]
        if info.isalpha():
            if not letter1:
                letter1=info
            else:
                letter2=info
        else:
            if not letter2:
                num1.append(int(info))
            else:
                num2.append(int(info))
    for i in num1:
        letter1 = letter1[:i+1]+letter1+letter1[i+1:]
    for i in num2:
        letter2 = letter2[:i+1]+letter2+letter2[i+1:]
    return letter1,letter2

#base algorithm
def base(string1,string2,gap,penalty):
    m = len(string1)
    n = len(string2)
    dp = [[None]*(m+1) for _ in range(n+1)]
    trackback = [[None]*(m) for _ in range(n)]
    for i in range(m+1):
        dp[0][i] = i*gap
    for i in range(n+1):
        dp[i][0] = i*gap
    for j in range(m+1):
        for i in range(n+1):         
            if dp[i][j] is None:           
                up = gap+dp[i-1][j]
                left = gap+dp[i][j-1]
                diag = penalty[string2[i-1]+string1[j-1]]+dp[i-1][j-1]
                choice = min(left,up,diag)  
                dp[i][j] = choice
                if choice == up:
                    trackback[i-1][j-1] = 'up'
                elif choice == left:
                    trackback[i-1][j-1] = 'left'
                else:
                    trackback[i-1][j-1] = 'diag'

    #dp and trackback are constructed. Now loop again to find path1 and path2.   
    track = []
    j,i = m-1,n-1
    while j >=0 and i >= 0:
        track.append(trackback[i][j])
        if trackback[i][j] == 'diag':
            i -= 1
            j -= 1
        elif trackback[i][j] == 'up':
            i -= 1
        else: 
            j -= 1
    
    path1,path2 = "",""
    i,j=0,0
    
    for t in track:
        
        if t == 'diag':
            path1 += string1[j]
            path2 += string2[i]
            i += 1
            j += 1
        if t == 'up':
            path1 += "_"
            path2 += string2[i]
            i += 1
        if t == 'left':
            path1 += string1[j]
            path2 += "_"
            j += 1
    
    return dp[n][m],path1,path2





    
    


