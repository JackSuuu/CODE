.data
	PI: .float 3.14
.text
	li $v0, 2 # 2 represents float
	lwc1  $f12, PI # f12 is in core processor
	syscall