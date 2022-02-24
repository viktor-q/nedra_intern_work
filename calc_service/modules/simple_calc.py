from calc_service.modules.round_upper import round_up


class Error(Exception):
    pass


class NotValidFirstSymbol(Error):
    pass


class NotValidOperators(Error):
    pass


class NotIdentifiedErrorInCalc(Error):
    pass


class SimpleCalculator:
    @round_up
    def calculation_from_string(self, input_string: str) -> str:
        first = ""
        second = ""
        operator = ""

        nums = "0123456789."
        operators = "+-/*"

        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }

        try:
            for element in input_string:
                if (first == "") and (element in "+-0123456789"):  # make first
                    first += element
                elif (first == "") and (element not in "+-01234567890"):
                    raise NotValidFirstSymbol  # custom exp

                elif (element in nums) and (operator == ""):
                    first += element
                elif (element in operators) and (operator == ""):
                    operator += element
                elif (element in nums) and (operator != ""):
                    second += element
                elif (element in operators) and (operator != ""):
                    try:
                        first = op[operator](float(first), float(second))
                        second = ""
                        operator = element
                    except:
                        raise NotValidOperators

            if (operator == "") and (second == ""):  # make end
                if (first[0] == "+") or (first == "-0"):
                    return first[1:]
                else:
                    return first
            else:
                first = op[operator](float(first), float(second))

            return first

        except NotValidFirstSymbol:
            raise NotValidFirstSymbol
        except NotValidOperators:
            raise NotValidOperators
        except Exception:
            raise NotIdentifiedErrorInCalc
