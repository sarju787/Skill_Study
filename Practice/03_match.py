
def http_error(status):
    match status:
        case 400:
            return "Bad Connection"
        case 401:
            return "Connection lost"
        case 402:
            return "i'am a good"
        case _:
            return "Someting new"

print(http_error(400))