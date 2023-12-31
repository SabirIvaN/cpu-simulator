# ----------------------------------------------------------------------------------
# USCC (Ultra Super Calculation Computer) Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+
# ----------------------------------------------------------------------------------

# CPU emulation class
class UltraSuperCalculator:

    # Class constructor method
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ""
        self.update_display(f"\nWelcome to { self.name }'s Calculator!\n")
    
    # Method to update the display
    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    # Method to store value for registration
    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        print("Binary", value_to_store)
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: { int(value_to_store, 2) } stored in Register: { self.numbers_index }.\n")
        self.numbers_index += 1

    # Method to load value from register
    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
    
    # Method for saving to history register
    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index
    
    # Method to add
    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value
    
    # Subtraction method
    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value
    
    # Method for multiplication
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value
    
    # Method for division
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = 0
        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1} / {num2}.\n")
        return calculated_value
    
    # Method for getting the last calculation
    def get_last_calculation(self):
        self.temp_history_index -= 1
        try:
            last_value = f"\nThe last calculated value was: {int(self.history_registers[self.temp_history_index], 2)}\n"
            self.update_display(last_value)
        except TypeError:
            print("\nNo further calculations stored.\n")

    # Method for Binary Reading
    def binary_reader(self, instruction):
        if len(instruction) != 32:
            self.update_display("\nInvalid Instruction Length\n")
            return
        opcode = instruction[0:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:]
        if opcode == "000001":
            self.store_value_to_register(store)
            return
        elif opcode == "100001":
            self.get_last_calculation()
            return
        elif opcode != "000000":
            self.update_display("\nInvalid OPCODE\n")
            return
        result = 0
        if function_code == "100000":
            print("Initiating Add Function")
            result = self.add(source_one, source_two)
        elif function_code == "100010":
            print("Initiating Subtract Function")
            result = self.subtract(source_one, source_two)
        elif function_code == "011000":
            print("Initiating Multiply Function")
            result = self.multiply(source_one, source_two)
        elif function_code == "011010":
            print("Initiating Divide Function")
            result = self.divide(source_one, source_two)
        else:
            self.update_display("\nInvalid Function\n")
            return
        self.store_to_history_register(result)
        self.update_display(f"The result is: { result }\n")

    # Method to view all numeric registers
    def view_all_number_registers(self):
        print(self.number_registers, "\n")

    # Method to view all history registers
    def view_all_history_registers(self):
        print(self.history_registers, "\n")