#include <iostream>
using namespace std;

#define MAX 20 //definimos la constante del valor max

class Pila {
   private:
      int arr[MAX];
      int top;
   public:
      Pila() {
         top = -1; //top nos lleva el control de cuantos elementos se agregaron
      }
      void push(int x) {
         if(top >= MAX-1) {
            cout << "No se puede agregar mas elementos. La pila está llena\n";
            return;
         }
         arr[++top] = x;
      }
      void pop() {
         if(top == -1) {
            cout << "No se puede eleminar elementos. La pila está vacía\n";
            return;
         }
         top--;
      }
      void print() {
         if(top == -1) {
            cout << "La pila está vacía\n";
            return;
         }
         cout << "Elementos dentro de la pila son:\n";
         for(int i = top; i >= 0; i--)
            cout << arr[i] << endl;
      }
};

int main() {
   Pila p;
   p.push(10);
   p.push(20);
   p.push(30);
   p.print();
   p.pop();
   p.print();
   return 0;
}
