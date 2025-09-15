from collections import Counter


def min_window_substring_loop(s: str, t: str) -> str:
    if s == "" or t == "":
        return ""

    t_counts: Counter[str] = Counter(t)
    candidates: list[str] = []

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if t_counts <= Counter(s[i:j]):
                candidates.append(s[i:j])

    return min(candidates, key=len, default="")


def min_window_substring_slide(s: str, t: str) -> str:
    if s == "" or t == "":
        return ""

    left: int = 0
    substr_counts: Counter[str] = Counter()
    target_counts: Counter[str] = Counter(t)
    min_substr: str = ""

    # NOTE: [left, right] are inclusive
    for right in range(len(s)):
        substr_counts[s[right]] += 1

        while target_counts <= substr_counts:
            if not min_substr or len(s[left : right + 1]) < len(min_substr):
                min_substr = s[left : right + 1]

            substr_counts[s[left]] -= 1
            left += 1

    return min_substr


min_window_substring = min_window_substring_slide


def test():
    # Basic examples
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "aa") == ""
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("ab", "a") == "a"
    assert min_window_substring("ab", "b") == "b"

    # Edge cases
    assert min_window_substring("", "a") == ""
    assert min_window_substring("a", "") == ""
    assert min_window_substring("", "") == ""

    # Multiple occurrences
    assert min_window_substring("aa", "aa") == "aa"
    assert min_window_substring("aaabbbccc", "abc") == "abbbc"
    assert min_window_substring("aaabbbccc", "aabbcc") == "aabbbcc"

    # Larger strings
    assert min_window_substring("xyzabcdabcbc", "abc") == "abc"
    assert min_window_substring("xyzzzzzzzzzzzzabc", "abc") == "abc"
    assert min_window_substring("xyzzzzzzzzzzzzabc", "zzabc") == "zzabc"


if __name__ == "__main__":
    min_window_substring("ADOBECODEBANC", "ABC")
