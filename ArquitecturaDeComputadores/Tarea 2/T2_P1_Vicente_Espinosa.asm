.globl start
.data 
	# ------ VIAJE -----
	N: .word 5 # Cantidad de amigos en el viaje
	amigues: .word 0, 1, 2, 3, 4, 5, 6 # ID de cada amigo (No se usa porque siempre van de a 1)
	G: .word 5 # Cantidad de gastos
	gastos: .float 0.0, 1000.0, -1.0,2.0, 2000.0, 2.0, 1.0, 2.0, 3.0, 5000.0, -1.0, 4.0, 20000.0, 4.0, 0.0, 2.0, 3.0, 4.0, 3.0, 20000.0, 4.0, 0.0, 2.0, 3.0, 4.0
	# -------END VIAJE----
	
	PrintDebeA: .ascii " debe a "
	PrintEspacio: .ascii " $"
	PrintNull: .ascii "\n"
	zeroFloat: .float 0.0
	menosUnoFloat: .float -1.0
	unoFloat: .float 1.0
	heap: .float 0.0 # inicio del heap
	
	
.text
	start:
	li a0, 0 # contador de cuantos monederos se han activado
	la a6, gastos # puntero de 'gastos'
	li a7, 0 #Lleva contador de cuantos gastos se han procesado
	
	for:
	# Para cargar todos los monederos en $0	
		lw t0, N # cargar N en t0 para comparar con contador
		beq a0, t0, cargarGasto #Si contador llega al final, pasar a ver gastos
		
		addi t1, zero, 4 # t1 = 4
		mul t1, a0, t1 # t1 = a0*4 (offset)
		la t2, heap # t2 = direccion inicial de monederos
		add t2, t2, t1 # t2 = posicion de monedero a0
		
		la t1, zeroFloat # t1 = zeroFloat address
		flw ft0, 0(t1) # ft0 = 0.0

		fsw ft0, 0(t2) # Cargar monedero de usuario numero a0 como $0
		addi a0, a0, 1 #Aumentar contador

		j for
		
	cargarGasto:
		lw t0, G # t0 = G
		beq t0, a7, generarPagos # if cantidad de gastos procesados == G, printear pagos
		addi a7, a7, 1 # Aumentar en 1 los gastos procesados
		flw ft0, 0(a6) # ft0 = quien pagó (id) en float
		fcvt.w.s t0, ft0 # t0 = id persona que pago en int

		addi a6, a6, 4 # Avanzar el puntero
		
		flw fa3, 0(a6) # fa3 = monto pagado
		li t2, 4 # t2 = 4
		mul t3, t2, t0 # t3 = offset para encontrar monedero de quien pagó (4*id)
		la t4, heap # t4 = address incio monedero
		add t2, t3, t4 # t2 = posicion de monedero de quien paga (offset + inicio)
		flw ft1, 0(t2) # ft1 = monedero actual de quien pago
		fadd.s ft2, fa3, ft1 # ft2 = monedero nuevo (monedero anterior + gasto)
		fsw ft2, 0(t2) # guardar monedero nuevo
		
		addi a6, a6, 4 # Avanzar el puntero
		flw fa2, 0(a6) # fa2 = cuantas personas participaron
		la t0, menosUnoFloat # t0 = menosUnoFloat adress
		flw ft1, 0(t0) # ft1 = -1.0
		feq.s t0, fa2, ft1 # t0 = (fa2 == ft1)
		beqz t0, noTodosPagan # if ft0 != -1.0, no todos pagan
		j todosPagan # else, todos pagan
	noTodosPagan:
		fdiv.s fa4, fa3, fa2 # fa4 = costo por persona (total/cantidad)
		la a0, heap # t4 = address incio monedero
		la t1, zeroFloat # t1 = address zeroFloat
		flw ft0, 0(t1) # t0 = contador de personas con monedero actualizado
		la t1, unoFloat # t1 = address unoFloat
		flw ft6, 0(t1) # ft6 = 1.0
		li t1, 4 # t1 = 4
		forNoTodos:
			feq.s t0, ft0, fa2 # t0 = (ft0 == fa2), si se cumple ya pasaron todos los pagos
			bne t0, zero, continuarGasto # si ya pasamos por todos (t0 == cantidad), terminar loop
			addi a6, a6, 4 # Avanzar a siguiente persona que gastó
			flw ft5, 0(a6) # ft5 = id persona en float
			fcvt.w.s t2, ft5 # t2 = id persona en int
			mul t3, t2, t1 # t3 = offset monedero (id*4)
			add t4, a0, t3 # t4 = posicion monedero  (inicial + offset)
			flw ft1, 0(t4) # ft1 = monedero actual persona
			fsub.s ft2, ft1, fa4 # ft2 = nuevo monedero de persona actual (monedero anterior - costo pp)
			fsw ft2, 0(t4) # actualizar nuevo monedero
			
			fadd.s ft0, ft0, ft6 # aumentar contador
			j forNoTodos

	todosPagan:
		lw t0, N # t0 = cantidad de personas en int
		fcvt.s.w ft1, t0 # ft1 = cantidad de personas en float
		fdiv.s fa4, fa3, ft1 # fa4 = costo por persona (total/total de personas)
		li t2, 0 # t2 = contador de personas con monedero actualizado
		la a0, heap # a0 = heap pointer
		forTodos:
			beq t0, t2, continuarGasto # si ya pasamos por todos (t2 == N), terminar loop
			li t4, 4 # t4 = 4
			mul t3, t2, t4 # t3 = offset monedero actual (index*4)
			add t4, t3, a0 # t4 = direccion monedero actual
			flw ft2, 0(t4) # ft2 = monedero actual persona actual
			fsub.s ft5, ft2, fa4 # ft5 = nuevo monedero de persona actual (monedero anterior - costo pp)
			fsw ft5, 0(t4) # actualizar nuevo monedero
			
			addi t2, t2, 1 # aumentar contador
			j forTodos
			
	continuarGasto:
		addi a6, a6, 4 # Avanzar el puntero a siguiente gasto
		j cargarGasto # Cargar nuevo gasto
		

			
	generarPagos:
		la t0, N # t0 = N address
		lw t1, 0(t0) # t1 = N
		la t0, menosUnoFloat # t0 = menosUnoFloat address
		flw fa5, 0(t0) # fa5 = -1.0 (para comparar)
		li a2, 0 # contador paga
		li a3, 0 # contador recibe
		li t4, 4 # t4 = 4
		buscarQuienPaga:
			bge a2, t1, fin # Si llega al final sin encontrar nada, terminar
			mul t0, a2, t4 # t0 = offset monedero
			add t5, t0, a0 # t5 = posicion monedero (offset + inicio)
			flw fa2, 0(t5) # fa2 = monedero persona actual
			la t0, zeroFloat # t0 = zeroFloat address
			flw ft1, 0(t0) # ft1 = 0.0
			fmin.s ft2, ft1, fa2 # ft2 = min(ft1, fa2)
			feq.s t0, ft2, ft1 # t0 = (min == 0.0)
			beqz t0, buscarQuienRecibe # if minimo no es 0.0, tiene monedero negativo
			addi a2, a2, 1 # aumentar contador
			j buscarQuienPaga
		buscarQuienRecibe:
			bge a3, t1, fin # Si llega al final sin encontrar nada, terminar (No deberia pasara acá)
			mul t0, a3, t4 # t0 = offset monedero
			add t5, t0, a0 # t5 = posicion monedero (offset + inicio)
			flw fa3, 0(t5) # fa3 = monedero persona actual
			la t0, zeroFloat # t0 = zeroFloat address
			flw ft1, 0(t0) # ft1 = 0.0
			fmax.s ft2, ft1, fa3 # ft2 = max(ft1, fa3)
			feq.s t0, ft2, ft1 # t0 = (max == 0.0)
			beqz t0, calcularPago # if maximo no es 0.0, tiene monedero positivo
			addi a3, a3, 1 # aumentar contador
			j buscarQuienRecibe
		calcularPago:
			la t0, menosUnoFloat # t0 = -1.0 address
			flw ft0, 0(t0) # ft0 = -1.0
			fmul.s ft1, ft0, fa2 # ft1 = cuanto debe quien paga en positivo
			fmin.s fa4, ft1, fa3 # numero menor entre cuanto debe y cuanto le deben a cada persona
			
			mul t0, a2, t4 # t0 = offset quien debe
			add t1, t0, a0 # posicion monedero quien debe
			flw ft0, 0(t1) # monedero actual de quien debe
			fadd.s ft1, ft0, fa4 # nuevo monedero de quien debe (anterior + pago)
			fsw ft1, 0(t1) # guardar nuevo monedero de quien debe
			
			mul t0, a3, t4 # t0 = offset a quien se le debe
			add t1, t0, a0 # posicion monedero a quien se le debe
			flw ft0, 0(t1) # monedero actual de a quien se le debe
			fsub.s ft1, ft0, fa4 # nuevo monedero de quien debe (anterior - pago)
			fsw ft1, 0(t1) # guardar nuevo monedero de a quien se le debe
			
			j printPago
	printPago:
	# print "a2 debe a a3 $fa4\n"
		mv a0, a2 # a0 = a2 
		li a7, 1 # printInt syscall
		ecall # print a2
		
		li a0, 1
		la a1, PrintDebeA # load address of PrintDebeA
		addi a2, zero, 8 # length text
		addi a7, zero, 64 # Write syscall
		ecall # print " debe a "
		
		mv a0, a3 # a0 = a3
		li a7, 1 # printInt syscall
		ecall # print a3
		
		li a0, 1
		la a1, PrintEspacio # load address of PrintEspacio
		addi a2, zero, 2 # length text
		addi a7, zero, 64 # Write syscall
		ecall # print " $"
		
		la t1, zeroFloat # t1 = zeroFloat address
		flw ft0, 0(t1) # ft0 = 0.0
		fadd.s fa0, ft0, fa4 # fa0 = fa4
		li a7, 2 # printInt syscall
		ecall # print fa4
		
		li a0, 1
		la a1, PrintNull # load address of PrintNull
		addi a2, zero, 1 # length text
		addi a7, zero, 64 # Write syscall
		ecall # print "\n"
		
		la a0, heap # reasignar a0 = inicio monederos

		j generarPagos
		
	fin:
		li	a7, 10 # syscall de exit
		ecall
