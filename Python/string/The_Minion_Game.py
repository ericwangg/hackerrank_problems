def minion_game(string):
    # your code goes here
    con_score = 0
    vow_score = 0
    vowels = [i for i in "aeiouAEIOU"]

    # substrings = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
    
    for i in range(len(string)):
        if string[i] in vowels:
            vow_score += len(string)-i
        else:
            con_score += len(string)-i

    if con_score > vow_score:
        print(f"Stuart {con_score}")
    elif con_score == vow_score:
        print("Draw")
    else:
        print(f"Kevin {vow_score}")

if __name__ == '__main__':
    s = input()
    minion_game(s)
