def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a matrix to store the length of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill in the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS
    lcs_length = dp[m][n]
    lcs = [""] * lcs_length
    
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the LCS and its length
    return "".join(lcs), len(lcs)

# Example usage:
str1 = "ACCTGAGGTA"
str2 = "CCTGGATCTT"
lcs, lcs_length = longest_common_subsequence(str1, str2)
print("Longest Common Subsequence:", lcs)
print("Length of LCS:", lcs_length)
