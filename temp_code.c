#include <stdio.h>
#include <string.h>

void safeFunction(char *input) {
    char buffer[10];  // Small buffer size
    // Use strncpy to avoid buffer overflow
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';  // Ensure null-termination
    printf("You entered: %s\n", buffer);
}

int main() {
    char userInput[100];
    printf("Enter some text: ");
    // Use fgets instead of gets to avoid buffer overflow
    fgets(userInput, sizeof(userInput), stdin);
    safeFunction(userInput);
    return 0;
}
