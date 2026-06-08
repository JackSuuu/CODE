.data
	array:   .word 1, 2, 3, 4, 5       # Define an array of 5 words
	arraySize: .word 5                # Define the size of the array

.text
main:
    la $a0, array                # Load the address of the array into $a0
    la $a1, arraySize            # Load the address of the array size into $a1
    lw $a1, 0($a1)               # Load the value of array size into $a1

    move $t0, $zero              # Initialize loop counter ($t0) to 0
loop:
    bge $t0, $a1, end_loop       # If counter >= array size, end loop
    lw $t1, 0($a0)               # Load the current element into $t1
    # ... Do something with $t1 ...
    addi $t0, $t0, 1             # Increment counter
    addi $a0, $a0, 4             # Move to the next element in the array (each word is 4 bytes)
    j loop                       # Jump back to the start of the loop
end_loop:
    # ... Continue with the rest of the` program ...

