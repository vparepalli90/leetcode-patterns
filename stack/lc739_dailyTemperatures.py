def dailyTemperatures(temperatures: list[int]) -> list[int]:
    sol =[0] * len(temperatures)
    if len(temperatures)== 0:
        return sol
    Stack = []
    for day,temp in enumerate(temperatures):
        while Stack and temp > temperatures[Stack[-1]]:
            lastday = Stack.pop()
            sol[lastday] = day - lastday
        Stack.append(day)
    return sol

if __name__ == "__main__":
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert dailyTemperatures([90, 80, 70]) == [0, 0, 0]
    print("lc739 dailytemperatures:All tests passed")