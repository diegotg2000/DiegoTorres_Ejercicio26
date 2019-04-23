graficas.png: graficador.py explicito.txt rk4.txt
	python graficador.py
explicito.txt rk4.txt: solucion.x
	./solucion.x
solucion.x: solucion.cpp
	g++ solucion.cpp -o solucion.x