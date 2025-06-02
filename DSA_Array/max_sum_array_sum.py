def max_sum_subarray_with_k_distinct(nums, k):
    from collections import defaultdict

    left = 0
    current_sum = 0
    max_sum = 0  # Empty subarray sum is valid
    freq_map = defaultdict(int)

    for right in range(len(nums)):
        current_sum += nums[right]
        freq_map[nums[right]] += 1

        # Shrink window if distinct elements exceed k
        while len(freq_map) > k:
            current_sum -= nums[left]
            freq_map[nums[left]] -= 1
            if freq_map[nums[left]] == 0:
                del freq_map[nums[left]]
            left += 1

        # If current_sum is negative, reset window
        if current_sum < 0:
            current_sum = 0
            freq_map.clear()
            left = right + 1
            continue

        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__=="__main__":
    A = [2,1,2,2,3,2,3,5,2,1,1,1]
    K=2
    print(max_sum_subarray_with_k_distinct(A,K))
