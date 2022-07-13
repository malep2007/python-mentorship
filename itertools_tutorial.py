import itertools
import operator

data = [3,4,6,2,1,9,0,7,5,8]
list(itertools.accumulate(data, operator.mul))

# Amortise a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print(list(itertools.accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))

# Chaotic recurrence relationship
logistic_map = lambda x, _: r*x*(1-x)
r = 3.8
x0 = 0.4

inputs = itertools.repeat(x0, 36)

print([format(x, '.2f') for x in itertools.accumulate(inputs, logistic_map)])
