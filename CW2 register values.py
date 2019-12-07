import math

# a program designed to obtain perfect values for a 200ms delay on the Arduino Nano

# the method for calulcating the delay in a triple nested loop with resets
def getDelayReset(a, b, c):
    # the formula that will be used
    finalValue = (((((a-1)*5)+4+5)*(b-1)+4+4+5)*(c-1)+4+4+4)-8 # the ret and call functions costs 4 and 4 cycles! Subtract that from +4 for last
    return finalValue

# the method for calulcating the delay in a triple nested loop without resets
def getDelayNoReset(a, b, c):
    # the formula that will be used
    finalValue = (((((a-1)*5)+4+5)*(b-1)+4+4+5)*(c-1)+4+4+4)-8 # the ret and call functions costs 4 and 4 cycles! Subtract that from +4 for last
    return finalValue

def getExactValue(target_value, error):
    count = 0
    for i in range(255):
        for j in range(255):
            for k in range(255):
                if (target_value-error) <= getDelayReset(i, j, k) <= (target_value+error):
                    count += 1
                    print("Value1: " + str(i) + " Value2: " + str(j) + " Value3: " + str(k))
                    print("Total amount of milliseconds delay is " + str(getDelayReset(i, j ,k)))
                    print(str(count) + "\n")

# 600ms delay
getExactValue(9600000, 4)

# 200ms delay
getExactValue(3200000, 4)
