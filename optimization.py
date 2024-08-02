import pulp


def main():
    
    prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    x1 = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    x2 = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    prob += x1 + x2, "Total_Profit"

    water_limit = 2 * x1 + x2 <= 100
    sugar_limit = x1 <= 50
    lemon_juice_limit = x1 <= 30
    fruit_puree_limit = 2 * x2 <= 40

    prob += water_limit, "Water_Constraint"
    prob += sugar_limit, "Sugar_Constraint"
    prob += lemon_juice_limit, "Lemon_Juice_Constraint"
    prob += fruit_puree_limit, "Fruit_Puree_Constraint"

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    print("Status:", pulp.LpStatus[prob.status])
    print("Optimal Production Quantity:")
    print(f"Lemonade: {pulp.value(x1):.0f}")
    print(f"Fruit Juice: {pulp.value(x2):.0f}")
    print(f"Total Profit: {pulp.value(prob.objective):.0f}")
    print(
        f"Unused resources: water {abs(pulp.value(water_limit)):.0f}; sugar {abs(pulp.value(sugar_limit)):.0f}; lemon "
        f"juice {abs(pulp.value(lemon_juice_limit)):.0f}; fruit puree {abs(pulp.value(fruit_puree_limit)):.0f}")


if __name__ == "__main__":
    main()
