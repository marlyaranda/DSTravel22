# from ejemplo_dos.models import Vuelo
#
# Vuelo(fechaPartida="2022-11-11", fechaArrivo="2022-11-11", destinoIda="Misiones", destinoVuelta="Cordoba", precio="123000", horaArrivo="15:00", horaPartida="16:00").save()
# Vuelo(fechaPartida="2022-10-10", fechaArrivo="2022-10-10", destinoIda="San Juan", destinoVuelta="Tucuman", precio="111000", horaArrivo="17:00", horaPartida="19:00").save()


from ejemplo_dos.models import Comprar
Comprar(NomPasajero="Juancito", ApePasajero="Lopez", DniPasajero="123123", FechaNacPas="1998-10-10", Email="prueba@prueba.com", Calle="122",Nro="124", Ciudad="Berisso", Provincia="Buenos Aires", Pais="Argentina", Telefono="1122334455", TitTarjeta="147258896", NroTarjeta="1111222233334444", DniTit="11223344", Vencimiento="2022-11-11", CVV="21").save()

print("Se cargo con éxito los usuarios de pruebas")

