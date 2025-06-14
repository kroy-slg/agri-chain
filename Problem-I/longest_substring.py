def longest_unique_substring(s: str):
    left = 0
    right = 0
    max_length = 0
    start_index = 0
    seen = set()

    while right < len(s):
        current_char = s[right]
        while current_char in seen:
            seen.remove(s[left])
            left += 1

        seen.add(current_char)

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left

        right += 1

    longest_substring = s[start_index:start_index + max_length]
    return max_length, longest_substring


if __name__ == "__main__":
    str1 = "abcabcbb"
    str2 = "bbbbb"


    for test_str in [str1, str2]:
        length, substring = longest_unique_substring(test_str)
        print(f"{test_str} -> Substring: '{substring}', Length: {length}")