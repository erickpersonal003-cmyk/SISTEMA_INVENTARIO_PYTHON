Algoritmo Sistema_Inventario_Basico
	Definir opcion Como Entero
	Definir nombreProducto, productoBuscar Como Cadena
	Definir cantidad, nuevaCantidad, cantidadVenta Como Entero
	Definir precio Como Real
	Definir productoRegistrado Como Lógico
	productoRegistrado <- Falso
	nombreProducto <- ''
	cantidad <- 0
	precio <- 0
	Repetir
		Escribir '======================================'
		Escribir '     SISTEMA BASICO DE INVENTARIO     '
		Escribir '======================================'
		Escribir '1. Agregar producto'
		Escribir '2. Mostrar inventario'
		Escribir '3. Buscar producto'
		Escribir '4. Actualizar cantidad'
		Escribir '5. Registrar venta o salida'
		Escribir '6. Mostrar productos con bajo stock'
		Escribir '7. Salir'
		Escribir 'Seleccione una opcion:'
		Leer opcion
		Según opcion Hacer
			1:
				Escribir 'Ingrese el nombre del producto:'
				Leer nombreProducto
				Escribir 'Ingrese la cantidad disponible:'
				Leer cantidad
				Escribir 'Ingrese el precio unitario:'
				Leer precio
				Si cantidad>=0 Y precio>=0 Entonces
					productoRegistrado <- Verdadero
					Escribir 'Producto agregado correctamente.'
				SiNo
					Escribir 'Error: la cantidad y el precio no pueden ser negativos.'
				FinSi
			2:
				Si productoRegistrado=Verdadero Entonces
					Escribir 'Producto registrado: ', nombreProducto
					Escribir 'Cantidad disponible: ', cantidad
					Escribir 'Precio unitario: $', precio
					Escribir 'Valor total del inventario: $', cantidad*precio
				SiNo
					Escribir 'No existen productos registrados.'
				FinSi
			3:
				Si productoRegistrado=Verdadero Entonces
					Escribir 'Ingrese el nombre del producto a buscar:'
					Leer productoBuscar
					Si productoBuscar=nombreProducto Entonces
						Escribir 'Producto encontrado.'
						Escribir 'Nombre: ', nombreProducto
						Escribir 'Cantidad: ', cantidad
						Escribir 'Precio: $', precio
					SiNo
						Escribir 'Producto no encontrado.'
					FinSi
				SiNo
					Escribir 'No existen productos registrados.'
				FinSi
			4:
				Si productoRegistrado=Verdadero Entonces
					Escribir 'Ingrese la nueva cantidad del producto:'
					Leer nuevaCantidad
					Si nuevaCantidad>=0 Entonces
						cantidad <- nuevaCantidad
						Escribir 'Cantidad actualizada correctamente.'
					SiNo
						Escribir 'La cantidad no puede ser negativa.'
					FinSi
				SiNo
					Escribir 'No existen productos registrados.'
				FinSi
			5:
				Si productoRegistrado=Verdadero Entonces
					Escribir 'Ingrese la cantidad vendida o retirada:'
					Leer cantidadVenta
					Si cantidadVenta>0 Entonces
						Si cantidadVenta<=cantidad Entonces
							cantidad <- cantidad-cantidadVenta
							Escribir 'Venta registrada correctamente.'
							Escribir 'Stock restante: ', cantidad
						SiNo
							Escribir 'No existe stock suficiente.'
						FinSi
					SiNo
						Escribir 'La cantidad debe ser mayor que cero.'
					FinSi
				SiNo
					Escribir 'No existen productos registrados.'
				FinSi
			6:
				Si productoRegistrado=Verdadero Entonces
					Si cantidad<=5 Entonces
						Escribir 'Alerta: producto con bajo stock.'
						Escribir 'Producto: ', nombreProducto
						Escribir 'Cantidad disponible: ', cantidad
					SiNo
						Escribir 'No existen productos con bajo stock.'
					FinSi
				SiNo
					Escribir 'No existen productos registrados.'
				FinSi
			7:
				Escribir 'Gracias por utilizar el sistema de inventario.'
			De Otro Modo:
				Escribir 'Opcion invalida. Intente nuevamente.'
		FinSegún
	Hasta Que opcion=7
FinAlgoritmo
