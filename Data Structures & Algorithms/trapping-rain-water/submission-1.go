func trap(height []int) int {
    ans := 0
    n := len(height)
    if n == 0 {
        return 0
    }

    lm := make([]int, n)
    rm := make([]int, n)

    lm[0] = height[0]
    for i:=1; i<n; i++ {
        lm[i] = max(lm[i-1], height[i])
    }

    rm[n-1] = height[n-1]
    for i:=n-2; i>=0; i-- {
        rm[i] = max(rm[i+1], height[i])
    }

    for i:=0; i<n; i++ {
        ans+= min(lm[i], rm[i]) - height[i]
    }

    return ans



}

