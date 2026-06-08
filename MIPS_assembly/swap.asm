.text 
	swap:
		# inputs: $a0 – array base, $a1 - index
		# Compute the address into the array
		sll $t0, $a1, 2   # reg $t0 = idx * 4
		add $t0, $a0, $t0 # reg $t0 = v + (idx*4)
		
				# $t0 holds the addr of v[idx]
				
		# Load the two values to be swapped
		lw $t1, 0($t0) # reg $t0 = v[idx]
		lw $t2, 4($t0) # reg $t2 = v[idx+1]
		
		# Store the swapped values back to memory
		sw $t2, 0($t0) # v[idx] = $t2
		sw $t1, 4($t0) # v[idx+1] = $t0