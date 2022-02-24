def round_up(foo_roundup_result):
    def wrapper(*args, **kwargs):
        number_for_round = foo_roundup_result(*args, **kwargs)
        if "." in str(number_for_round):
            before_dot = str(number_for_round).split(".")[0]
            after_dot = str(number_for_round).split(".")[1]
            if len(after_dot) <= 3:
                if after_dot == "0":
                    return str(before_dot)
                else:
                    return str(number_for_round)
            else:
                if int(after_dot[3]) >= 5:
                    result_after_dot = int(after_dot[:3]) + 1
                    number_for_round = str(before_dot) + "." + str(result_after_dot)
                    return str(float(number_for_round))
                else:
                    number_for_round = str(before_dot) + "." + str(after_dot[:3])
                    return str(number_for_round)
        else:
            return str(number_for_round)

    return wrapper
