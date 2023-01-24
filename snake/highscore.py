def get_high_score():
    with open("high_score.txt") as file:
        content = file.read()
        space_index = content.index(" ")
        content_len = len(content)
        s1 = slice(space_index+1, content_len, 1)
        score = int(content[s1])
        file.close()
        return score


def save_high_score(score):
    with open("high_score.txt", mode="w") as file: #a is for append, w for write
        content_to_save = f"highscore: {score}"
        file.write(content_to_save)
        file.close()
