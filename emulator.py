# emulator.py
def emulate_stack(parsed_code):
    """
    Simulates stack behavior based on function invocations and simulates potential overflows.
    """
    stack = []
    for func, _ in parsed_code:
        stack.append(f"Simulating stack for function '{func}'")
        if "strcpy" in func or "gets" in func:
            stack.append(f"Warning: Possible buffer overflow in '{func}'")
    return stack
