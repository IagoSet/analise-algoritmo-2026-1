import math

def f_recursiva(n):
    if n == 1:
        return 2
    else:
        return 2 * f_recursiva(n - 1) + n**2

def main():
    try:
        n = int(input("Digite o valor de n (inteiro positivo): "))
        
        if n < 1:
            print("Por favor, insira um valor maior ou igual a 1.")
        else:
            resultado = f_recursiva(n)
            print(f"\nO resultado de F({n}) via recursão é: {resultado}")
            
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()