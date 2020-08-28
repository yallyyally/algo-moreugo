def solution(phone_book):
    answer = True

    for x in range(len(phone_book)):
        for y in range(x + 1, len(phone_book)):
            if len(phone_book[x]) <= len(phone_book[y]):
                if phone_book[y].find(phone_book[x]) != -1:
                    answer = False
                    break
            else:
                if phone_book[x].find(phone_book[y]) != -1:
                    answer = False
                    break
        if answer == False:
            break

    return answer