def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        # If current string is valid and complete
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add '(' if possible
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # Add ')' if possible
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# Example usage:
n = 3
output = generate_parentheses(n)
for combo in output:
    print(combo)
