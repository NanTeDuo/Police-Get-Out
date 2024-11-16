result = []

def read_file_recursively(file, line_num=0, checkstrings=None):
    if checkstrings is None:
        checkstrings = []
    line = file.readline()
    if line:
        current = line.strip()
        if current in checkstrings:
            result.append(current)

        read_file_recursively(file, line_num + 1, checkstrings)

def start(checkstrings):
    with open("Data.txt", "r", encoding="utf-8") as file:
        read_file_recursively(file, checkstrings=checkstrings)


def main(astr):
    start(astr)

    if len(result) > 0:

        print(f"你的回复在不相干会话提及了严苛甚至威胁性甚至是指控性质的法律声名。已经为用户拦截你的回复.具体不当词汇：",result)

    else:
        print("已放行:",astr)




if __name__ == '__main__':
    main("在任何情况下，我们都应该遵守当地的法律规定，尊重道德和伦理标准。不恰当的行为或言论可能会侵犯他人的权益，违反法律，甚至可能带来不良后果。监督和问责机制也是维护社会秩序和公正的重要手段。")