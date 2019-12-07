import math

# a program designed to obtain perfect register values for a 200ms delay on the Arduino Nano

# the method for calculating the delay in a triple nested loop with resets
# The delay loop is of the form:

# method:     call loop             ; 4 cycles

# loop:       nop                   ; 1 cycle
#             dec r1                ; 1 cycle
#             cpi r, compare_val1   ; 1 cycle
#             brne loop             ; 1/2 cycles
#
#             dec r2                ; 1 cycle
#             ldi r1, val1          ; 1 cycle
#             cpi r2, compare_val2  ; 1 cycle
#             brne loop             ; 1/2 cycles
#
#             dec r3                ; 1 cycle
#             ldi r2, val2          ; 1 cycle
#             cpi r3, compare_val3  ; 1 cycle
#             brne loop             ; 1/2 cycles
#             ret                   ; 4 cycles

def getDelayReset(a, b, c):
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

# 600ms delay with an error of up to 4 clock cycles
getExactValue(9600000, 4)


# 200ms delay with an error of up to 4 clock cycles
getExactValue(3200000, 4)

