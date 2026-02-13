# arr = [2,1,5,1,3,2]
# k = 3

# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum += arr[i]      # add next
#     window_sum -= arr[i-k]    # remove first
    
#     max_sum = max(max_sum, window_sum)

# print(max_sum)

def longest_unique(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right-left+1)

    return max_len

print(longest_unique("bacabcbb"))
