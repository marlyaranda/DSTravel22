from ejemplo.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=567567).save()


from ejemplo_dos.models import Vuelo

Vuelo(fechaPartida="2022-11-11", fechaArrivo="2022-11-11", destinoIda="Salta", destinoVuelta="Cordoba", precio="123000", horaArrivo="15:00", horaPartida="16:00").save()
Vuelo(fechaPartida="2022-10-10", fechaArrivo="2022-10-10", destinoIda="Mendoza", destinoVuelta="Tucuman", precio="111000", horaArrivo="17:00", horaPartida="19:00").save()

print("Se cargo con éxito los usuarios de pruebas")

