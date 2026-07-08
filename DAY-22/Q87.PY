def character_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def main():
    text = "apple"
    result = character_frequency(text)
    print(result)

main()
