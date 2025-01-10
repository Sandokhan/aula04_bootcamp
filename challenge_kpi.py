def calculate_kpi(nome: str, salario: float, bonus: float) -> dict:
    kpi_dict : dict = {}

    nome_valido : bool = False
    salario_valido : bool = False
    bonus_valido : bool = False

    while not nome_valido:
        try:
            name : str = nome

            # Verifica se o nome está vazio
            if len(name) == 0:
                raise ValueError("O nome não pode estar vazio.")
            # Verifica se há números no nome
            elif any(char.isdigit() for char in name):
                raise ValueError("O nome não deve conter números.")
            else:
                kpi_dict["nome"] = name
                nome_valido : bool = True
        except ValueError as e:
            print(e)
            exit()

    while not salario_valido:
        try:
            salary: float = float(salario)
            if salary < 0:
                print("Por favor, digite um valor positivo para o salário.")
                break
            else:
                kpi_dict["salario"] = salary
                salario_valido : bool = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")
            exit()

    while not bonus_valido:
        try:
            bonus_rate : float = float(bonus)
            if bonus_rate < 0:
                print("Por favor, digite um valor positivo para o bônus.")
                break
            else:
                # Calculate the bonus received
                bonus_recebido : float = 1000 + salary * bonus_rate
                kpi_dict["bonus"] = bonus_recebido
                bonus_valido : bool = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")
            exit()

    if nome_valido and salario_valido and bonus_valido:
        return kpi_dict
    else:
        return "Três são necessários para o calculo do KPI."

# Teste
# print(calculate_kpi("João", 10000, 1.5))
# print(calculate_kpi("João", -10000, 1.5))
# print(calculate_kpi("Jo4o", 10000, 1.5))
print(calculate_kpi("João", 10000, -1.5))