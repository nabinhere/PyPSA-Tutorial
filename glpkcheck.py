from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals, minimize

# Create a simple optimization model
model = ConcreteModel()
model.x = Var(within=NonNegativeReals)
model.obj = Objective(expr=model.x, sense=minimize)

# Use GLPK solver
solver = SolverFactory('glpk')
results = solver.solve(model)

# Print the results
print(results)
