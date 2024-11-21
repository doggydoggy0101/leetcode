# Run test cases.
#
# Arguments
#
# - `fn_solution`     - Function to be verified.
# - `list_test_case` - List of turples of input/output.
def runTestCases(fn_solution, list_test_case):
    for idx, (data, expected) in enumerate(list_test_case):
        # ensure data is a tuple to avoid unpacking list inputs
        if not isinstance(data, tuple):
            data = (data,)
        try:
            result = fn_solution(*data)  # unpack inputs
            if result == expected:
                print("Test case {}: Passed".format(idx + 1))
            else:
                print("Test case {}: Failed".format(idx + 1))
                print(
                    "-- Input: {}, Output: {} Expected: {}".format(
                        data, result, expected
                    )
                )
        except Exception as e:
            print("Test case {}: Failed".format(idx + 1))
            print("-- Error: {}".format(str(e)))
