def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    required = len(dict_t)
    formed = 0

    window_start = 0
    window_end = 0

    window_counts = {}

    ans = float('inf'), None, None

    while window_end < len(s):
        character = s[window_end]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while formed == required:
            character = s[window_start]

            if window_end - window_start + 1 < ans[0]:
                ans = (window_end - window_start + 1, window_start, window_end)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            window_start += 1

        window_end += 1

    return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]