.data

    timeNow:.word 0xFFFF0018
    cmp:    .word 0xFFFF0020
    AskForTime:      .ascii "\nIngrese un tiempo: \n"
    PrintTime1: .ascii "Han pasado "
    PrintTime2: .ascii " segundos!"
    
.text
    main:
    	
    	# pedir input por primera vez
    	addi a0, zero, 1
		la a1, AskForTime # load address of AskForTime
		addi a2, zero, 21
		addi a7, zero, 64 # linux write system call
		ecall
		
		addi a7, zero, 5 # ReadInt
        mv a0, zero
        ecall # obtener int de input, guardar en a0
        mv a3, a0 # guardar tiempo en a3
    	
        # armar el timer para que dure a3 segundos
		lw a0 timeNow
		lw t2 0(a0)
		li t0, 1000
		mul t1, a3, t0 # se usa a3*1000
		add t1 t2 t1
		lw t0 cmp
		sw t1 0(t0)
        
        # setear la direccion del handler y activamos las interrupciones
        la	t0, handle
        csrrs	zero, 5, t0
        csrrsi	zero, 4, 0x10
        csrrsi	zero, 0, 0x1
        
        mv a5, zero #Se marca a5 como 0 (marca si es la primera ejecucion)
        
        
    loop:
        nop
        j	loop


    handle:
      
        
        #printear tiempo que pasó
        addi a0, zero, 1
		la a1, PrintTime1 # load address of PrintTime1
		addi a2, zero, 11
		addi a7, zero, 64 # linux write system call
		ecall
		
		mv a0, a3 #Se carga el int de la llamada anterior
		addi a7, zero, 1 # linux print int system call
		ecall
		
		
		addi a0, zero, 1
		la a1, PrintTime2 # load address of PrintTime2
		addi a2, zero, 10
		addi a7, zero, 64 # linux write system call
		ecall
        
    	
        # Preguntamos por nuevo tiempo
        addi a0, zero, 1
		la a1, AskForTime # load address of AskForTime
		addi a2, zero, 21
		addi a7, zero, 64 # linux write system call
		ecall
		
		addi a7, zero, 5 # ReadInt
        mv a0, zero
        ecall # get int from console, store in a0
        mv a3, a0 # guardar tiempo en a3
        
		mv t0, zero
		ble a3, t0, exit # if input <= 0: terminar
        
        
        # rearmar el timer para que dure a3 segundos
		lw a0 timeNow
		lw t2 0(a0)
		li t0, 1000
		mul t1, a3, t0
		add t1 t2 t1
		lw t0 cmp
		sw t1 0(t0)
        
        uret

    exit:
        li	a7, 10
        ecall
