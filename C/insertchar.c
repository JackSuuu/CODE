#include <stdio.h>
#include <string.h>

/*
 * Function to insert a character 'c' at position 'pos' in string 's'.
 * Arguments:
 *   c   - the character to insert
 *   pos - the 0-based index where the character is to be inserted
 *   s   - the null-terminated string
 * Returns:
 *   0 if insertion is successful, or -1 if an error occurs.
 */
int insertchar(char c, int pos, char *s) {
    // Step 1: Calculate the current length of the string
    int length = strlen(s);

    // Step 2: Check if position is valid
    if (pos < 0 || pos > length) {
        return -1; // Invalid position
    }

    // Step 3: Shift characters to the right to make space for the new character
    for (int i = length; i >= pos; i--) {
        s[i + 1] = s[i]; // Move each character one position to the right
    }

    // Step 4: Insert the new character at the specified position
    s[pos] = c;

    // Step 5: Return success
    return 0;
}

// Example usage
int main() {
    char str[100] = "HelloWorld"; // The string must have enough space to accommodate the new character
    char ch = 'X';
    int position = 5;

    if (insertchar(ch, position, str) == 0) {
        printf("Modified string: %s\n", str); // Output: "HelloXWorld"
    } else {
        printf("Error: Invalid position!\n");
    }

    return 0;
}
