def min_substring_to_shuffle(s):
    """
    Calculates the minimum length of a contiguous substring to shuffle to make a palindrome.

    Args:
        s: The input string.

    Returns:
        The minimum length of the substring to shuffle.
    """
    n = len(s)
    if n <= 1:
        return 0  # Already a palindrome or empty

    # Create a DP table to store LPS lengths
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Iterate through the DP table diagonally
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                if cl == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Return the minimum length of substring to shuffle
    return n - dp[0][n - 1]


if __name__=="__main__":
    s = input()
    print(min_substring_to_shuffle(s))