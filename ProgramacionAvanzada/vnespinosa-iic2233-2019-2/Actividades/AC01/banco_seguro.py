from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        Cliente.__init__(self,id_cliente,nombre,contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.__saldo_actual

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        if float(nuevo_saldo) < float(0):
            self.tiene_fraude = True


    def deposito_seguro(self, dinero):
        super().depositar(dinero)
        self.saldo_actual += dinero
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            archivo.write(super().id_cliente,"deposita",dinero)

    def retiro_seguro(self, dinero):
        if not super().tiene_fraude:
            super().retirar(dinero)
            saldo_actual -= dinero
            ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
            with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
                archivo.write(super().id_cliente,"retira",dinero)


class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        BancoDCC.__init__(self)

    def cargar_clientes(self, ruta):
        file = open(ruta)
        for i in file:
            i = ClienteSeguro()
            super().clientes.append(i)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        if accion == "retirar":
            super().retiro_seguro(dinero)
        elif accion == "depositar":
            super().deposito_seguro(dinero)

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        for transaccion in historial:
            lista = transaccion.split(",")
            id = lista[0]
            accion = lista[1]
            monto = lista[2]
            self.realizar_transaccion(id,accion,monto)

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        file = open(ruta)
        for line in ruta:
            lista = line.split(",")
            if int(super().saldo_actual()) != int(lista[2]):
                super().tiene_fraude = True
