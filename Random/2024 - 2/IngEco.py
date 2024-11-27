
class Operation:
    def __init__(self, given_var: float = None, wanted_operation: str = None, interest: float = None, periods: int = None) -> None:
        self.__given_var: float = given_var
        self.__wanted_operation: str = wanted_operation
        self.__interest: float = interest
        self.__periods: int = periods


    @property
    def given_var(self):
        return self.__given_var

    def operate(self):
        try:
            match self.__wanted_operation:
                case "f/p":
                    return self.__given_var * ((1 + self.__interest)**self.__periods)

                case "p/f":
                    return self.__given_var * (1/((1 + self.__interest)**self.__periods))
                
                case "f/a":
                    return self.__given_var * (((1 + self.__interest)**self.__periods)-1)/self.__interest

                case "a/f":
                    return self.__given_var * (self.__interest/(((1 + self.__interest)**self.__periods)-1))

                case "a/p":
                    return self.__given_var * ((self.__interest * ((1 + self.__interest)**self.__periods))/(((1 + self.__interest)**self.__periods)-1))

                case "p/a":
                    return self.__given_var * ((((1 + self.__interest)**self.__periods)-1)/(self.__interest * ((1 + self.__interest)**self.__periods)))

                # In Process

                case "g/a":
                    return None



                case _:
                    print("Invalid Operation")


        except Exception as e:
            print(f"Something happend {e}")

if __name__ == "__main__":
    
    pass