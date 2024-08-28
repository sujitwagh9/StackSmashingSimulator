# protector.py
def demonstrate_protection(stack_emulation):
    """
    Shows stack protection mechanisms such as stack canaries.
    """
    protections = []
    for step in stack_emulation:
        protections.append(f"Applying protection to {step}")
    return "\n".join(protections)
