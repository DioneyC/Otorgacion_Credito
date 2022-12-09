# Aprobación de crédito
API diseñada para otorgar o rechazar crédito de un postulante en base a una serie de requisitos. La API está diseñada en Python con Flask mientras que la interacción con el Front es mediante javascript. 

Contexto: La API es para aceptar o rechazar dar un crédito a una persona, los datos de
entrada serán los siguientes:
* Primer nombre.
* Apellido paterno.
* Apellido materno.
* Fecha de nacimiento (DD-MM-YYYY).
* Ingresos mensuales.
* Numero de dependientes económicos

Reglas
* Si el ingreso es mayor a $25,000 aprobar crédito.
* Si el ingreso esta entre $15,000 y $25,000, validar que el número de dependiente
sea menor a 3, aprobar crédito.
* Si es menor a $15,000 no aprobar el crédito.
* Con la información obtenida tendrá que calcular el RFC sin homoclave (ver
ejemplo).
* Por último, debe hacer un insert a la base de datos con las siguientes columnas:
o (ID, PRIMER_NOMBRE, APELLIDO_PAT, APELLIDO_MAT, FECHA_NAC, RFC,
INGRESOS_MENSUALES, DEPENDIENTES, APROBADO)
* La respuesta de la API serán los siguientes tres datos:
o ID
o RFC
o Aprobado o rechazado
