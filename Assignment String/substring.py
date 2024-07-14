def check_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

# Example usage
main_string = "Hello, how are you today?"
sub_string = "how are you"

if check_substring(main_string, sub_string):
    print(f"'{sub_string}' is present in the main string.")
else:
    print(f"'{sub_string}' is not present in the main string.")

