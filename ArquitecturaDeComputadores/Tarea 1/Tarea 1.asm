.globl  start
.data
    # --- TERREMOTO ---
    I: .word 82, 17, 1 # porcentajes de cada uno de los ingredientes, siempre suman 100 (H, P, G)
    # No modificar
    Wa: .word 7, 3, 2 	# pesos w_a para el primer perceptron
    Wb: .word 4, 2, 8 	# pesos w_b para el segundo perceptron
    U:  .word 150 		# umbral
    # --- END TERREMOTO ---
    # de aca para abajo van sus variables en memoria
.text
    start:
        la s1, Wa
        funcion_de_activacion:
        	jal ra, paso_sinaptico
        	lw t0, U
        	ble a5, t0, menor_helper # if a5 < umbral,saltar a menor_igual
        	bgt a5, t0, mayor_helper # else, saltar a mayor
        	continuar:
        		la t0, Wb
       			beq s1, t0, cumple # Si ya revisamos Wa y Wb,significa que esta bueno
       			la s1, Wb # Si aun no revisamos Wb, lo cargamos
       			j funcion_de_activacion

        mayor_helper:
        	jal ra, mayor
        	j continuar

       	menor_helper:
        	jal ra, menor_igual
        	j continuar

        mayor:
        	mv s2, ra
        	jal ra, modular_exp_3
        	mv a6, a0
        	li a2, 3
        	jal ra, mod
        	ble a1, zero, no_cumple # Si es <= a 0 entonces esta malo

        	jalr zero, 0(s2) # Si esta bueno volvemos al incio

        menor_igual:
        	mv s2, ra
        	mv a2, a6
        	addi a6, a6, -1
        	jal ra, mod
        	ble a1, zero, no_cumple # Si es <= a 0 entonces esta malo

        	jalr zero, 0(s2) # Si esta bueno volvemos al incio

       	no_cumple:
       		mv a0, zero  # El terremoto esta malo
       		j end

       	cumple:
       		li a0, 1 # El terremoto esta bueno
       		j end


	paso_sinaptico: # Calcula la ponderacion de ingredientes con las proporciones en s1, output en a5
		la t0, I
		lw  a2, 0(t0) # a2 = H
		lw a3, 4(t0) # a3 = P
		lw a4, 8(t0) # a4 = G
		lw t3, 0(s1) # t3 = w_1_H
		lw t4, 4(s1) # t4 = w_1_P
		lw t5, 8(s1) # t5 = w_1_G
		li a5, 0 # Resutado suma funcion de activacion
		mul t6, a2, t3
		add a5, zero, t6
		mul t6, a3, t4
		add a5, a5, t6
		mul t6, a4, t5
		add a5, a5, t6

		jalr zero, 0(ra) # Volver a donde se llamo


	modular_exp_3: # 3^a5 mod a5 y retorna en a0
		mv s0, ra
		li a0, 1
		li a3, 1 # Contador para el while
		mv a2, a5
		while: # a3 < x = a5
			li t0, 3
			mul a6, t0, a0
			jal ra, mod
			mv a0, a1
			bge a3, a5, volver # termina si a3 > x
			addi a3, a3, 1 #aumentar contador
			j while

	mod: # a6 mod a2 y se retorna en a1
		div t1, a6, a2
		mul t2, t1, a2
		sub a1, a6, t2
		ret

	volver: #retorna a la funcion que lo haya llamado
		jalr zero, 0(s0)

	end:
	