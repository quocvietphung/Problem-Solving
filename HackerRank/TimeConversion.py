class TimeConversion:
    def __init__(self):
        self.time_string = ""

    def get_time_string(self):
        self.time_string = input("Enter a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM): ")

    def convert_time(self):
        hour, minute, second = map(int, self.time_string[:-2].split(":"))
        meridiem = self.time_string[-2:]

        if meridiem == "AM":
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour += 12

        return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)

    def print_result(self):
        result = self.convert_time()
        print("The time in 24-hour clock format is:", result)

# Test the code
tc = TimeConversion()
tc.get_time_string()
tc.print_result()
