.data
	myMessage: .asciiz "Hello Assembly!\n" 

.text
main:

    	li $v0, 4 # load immediate a register value
    	la $a0, myMessage # load address of myMessage
    	syscall



    # Other code...