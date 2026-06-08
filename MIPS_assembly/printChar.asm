.data
	myCharacter: .byte 'm'

.text
    	li $v0, 4 # load immediate a register value
    	la $a0, myCharacter # load address of myMessage
    	syscall