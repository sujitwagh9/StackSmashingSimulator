# protector.py
def demonstrate_protection(stack_emulation):
    """
    Demonstrates stack protection mechanisms, such as stack canaries, to prevent overflows.
    """
    protections = []
    for step in stack_emulation:
        if "overflow" in step:
            protections.append(f"Protection applied to prevent overflow in {step}")
        else:
            protections.append(f"No protection needed for {step}")
    return "\n".join(protections)
