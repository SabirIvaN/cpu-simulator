#!/usr/bin/env python3

# Importing the emulating CPU class
from modules.calculators import UltraSuperCalculator;

# Creating an instance of a class
my_calculator = UltraSuperCalculator("Ivan")

########################################### ---- BINARY TEMPLATE --- ####################################
# Binary code example for Adding values at index 1 and 2 in numbers_register together
# 000000 00001 00010 0000000000 100000
# -------------------------------------------------------------------------------------------------------
# This is the OPCODE and it is urrently set to Add / Subtract / Multiply / Divide instructions. 
# Modify OPCODE to store value to next register or return previous calculation. 
# 000000
# -------------------------------------------------------------------------------------------------------
# Currently set to numbers_register index position of 1, modify to point to specific address in register. 
# If your OPCODE is 000001 (store in next register) or 100001 (return previous calculation), set this 
# section binary to all zeros, 000000.
# 00001
# -------------------------------------------------------------------------------------------------------
# Currently set to numbers_register index position of 2, modify to point to specific address in register. 
# If your OPCODE is 000001 (store value to next register) or 100001 (return previous calculation), set 
# this binary section to all zeros, 000000.
# 00010 = int 2
# -------------------------------------------------------------------------------------------------------
# Store in number_register - If your OPCODE is 000001, change this portion of the binary
# to represent the number you want stored in the number_register. e.g. 0000000101 = 5
# 0000000000
# -------------------------------------------------------------------------------------------------------
# FUNCTION code which is currently set to Add. Modify FUNCTION code to either Subtract,  
# Multiply, Divide. Or change it so you can Store value to next register or return the 
# previous calculation.   
# 100000
# -------------------------------------------------------------------------------------------------------
#########################################################################################################

# Adds 5 and 10 to number registers
my_calculator.binary_reader("00000100000000000000000101000000")
my_calculator.binary_reader("00000100000000000000001010000000")

# Add 6 and 22 to number registers
my_calculator.binary_reader("00000100000000000000000110000000")
my_calculator.binary_reader("00000100000000000000010110000000")
my_calculator.view_all_number_registers()

# Add 10 and 6 
my_calculator.binary_reader("00000000010000110000000000100000")

# Subtract 10 from 22
my_calculator.binary_reader("00000000100000100000000000100010")

# Multiply 6 and 5
my_calculator.binary_reader("00000000011000010000000000011000")

# Divide 10 by 5
my_calculator.binary_reader("00000000010000010000000000011010")

# Adds/Subtracts/Multiplies/Divides 5 and 10 from registers
my_calculator.binary_reader("00000000001000100000000000100000")
my_calculator.binary_reader("00000000001000100000000000100010")
my_calculator.binary_reader("00000000001000100000000000011000")
my_calculator.binary_reader("00000000001000100000000000011010")

# Gets the last three calculations
my_calculator.binary_reader("10000100000000000000000000000000")
my_calculator.binary_reader("10000100000000000000000000000000")
my_calculator.binary_reader("10000100000000000000000000000000")

my_calculator.view_all_number_registers()
my_calculator.view_all_history_registers()

# Error testing
my_calculator.binary_reader("1234567812345678123456781234567") # Induces Invalid OPCODE Error
my_calculator.binary_reader("12345678123456781234567812345678") # Induces Invalid OPCODE Error
my_calculator.binary_reader("00000078123456781234567812345678") # Induces Invalid FunctionError
my_calculator.binary_reader("00000000011000000000000000011010") # Division by 0 Error
my_calculator.binary_reader("00000000000000000000000000011010") # Division by 0 Error