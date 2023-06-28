#include <iostream>
#include <string>
using namespace std;

int main() {
	stack<string> pila;
    int cantidad_nombres_iguales = 0;
    int cantidad_nombres_L = 0;
    int cantidad_total_nombres = 0;
    string nombre;
   int opcion;
   Pila p;
   while (opcion != 4) {
        cout << "1. Insertar un elemento en la pila" << endl;
        cout << "2. Eliminar un elemento de la pila" << endl;
        cout << "3. Mostrar elementos de la pila" << endl;
        cout << "4. Salir" << endl;
        cout << "Ingrese una opcion: ";
        cin >> opcion;
        switch (opcion) {
            case 1:{
            	// Pedir la cantidad de nombres a ingresar
				int cantidad_nombres;
    			cout << "Ingresa la cantidad de nombres a ingresar: ";
    			cin >> cantidad_nombres;

                cout << "Ingrese el elemento a insertar: \n";
                string elemento;
                cin >> elemento;// Se aplica un enqueue
                p.push(elemento);//Se aplica un push que agrega al final de la cola el elemento a guardar
                break;
				}
            case 2:{
            	p.pop();
                break;
				
			}
               	
            case 3:{
            	p.print();
            	cout << "Cantidad de nombres iguales: " << p.compare(p.arr[0], p.arr[1]) + p.compare(p.arr[1], p.arr[2]) + p.compare(p.arr[2], p.arr[3]) << endl;
   				cout << "Cantidad de nombres que inician con L: " << p.getCountL() << endl;
                break;
				}
            case 4:
                break;
            default:
                cout << "Opción inválida" << endl;
        }
    }
   
   return 0;
}
