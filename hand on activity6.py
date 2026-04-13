import time
import dis

# Function 1: Writing (3 tasks with delay)
def writing():
    print("Writing Task 1...")
    time.sleep(1)

    print("Writing Task 2...")
    time.sleep(1)

    print("Writing Task 3...")
    time.sleep(1)



def reading():
    print("Reading Task 1...")
    time.sleep(1)

    print("Reading Task 2...")
    time.sleep(1)

    print("Reading Task 3...")
    time.sleep(1)



writing()
reading()


print("\nDisassembly of writing():")
dis.dis(writing)

print("\nDisassembly of reading():")
dis.dis(reading)


def analyze(func):
    instructions = list(dis.get_instructions(func))
    
    total_instructions = len(instructions)
    

    lookup_ops = ["LOAD_GLOBAL", "LOAD_NAME", "LOAD_ATTR"]
    lookup_count = sum(1 for instr in instructions if instr.opname in lookup_ops)

    print(f"\nAnalysis of {func.__name__}:")
    print(f"Total Instructions: {total_instructions}")
    print(f"Total Lookups: {lookup_count}")
    
    
    return total_instructions, lookup_count

w_instr, w_lookup = analyze(writing)
r_instr, r_lookup = analyze(reading)

total_instr = w_instr + r_instr
total_lookup = w_lookup + r_lookup

print("\nCombined Totals")
print(f"Total Instructions writing + reading: {total_instr}")
print(f"Total Lookups writing + reading: {total_lookup}")