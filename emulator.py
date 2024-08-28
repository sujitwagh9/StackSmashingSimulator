# emulator.py
def emulate_stack(parsed_code):
    """
    Simulates the stack behavior for the parsed code, visualizing stack frames and overflows.
    """
    stack = []
    for func in parsed_code:
        stack.append(f"Simulating {func}")
    return stack
