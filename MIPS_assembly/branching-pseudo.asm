.data
    message: .asciiz "Hi, how are you"
.text
    main:
        addi $s0, $zero, 14      # Set $s0 to 14
        addi $s1, $zero, 10       # Set $s1 to 10

        bgt $s0, $s1, displayHi   # Branch to displayHi if $s0 > $s1

    # end of main
    li $v0, 10                  # Set $v0 to 10 for syscall exit
    syscall                     # Perform the syscall

    displayHi:
        li $v0, 4                # Set $v0 to 4 for syscall print_string
        la $a0, message          # Load the address of message into $a0
        syscall                  # Perform the syscall to print the message
