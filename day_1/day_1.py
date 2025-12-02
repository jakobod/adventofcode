import argparse

def parse_input(lines, starting_point = 50):
  current_pos = starting_point
  zero_count = 0

  for l in lines:
    l = l.strip()
    direction = l[0]
    amount = int(l[1:])
    if direction == "L":
      print(f"Rotate {-amount}")
      current_pos -= amount
    elif direction == "R":
      print(f"Rotate {amount}")
      current_pos += amount

    current_pos = current_pos % 100

    if current_pos == 0:
      zero_count += 1
    
    
    print(f"Current Position = {current_pos}")
  print(f"Password is {zero_count}")


def parse_input_sophisticated(lines, starting_point = 50):
  current_pos = starting_point
  zero_count = 0

  for l in lines:
    l = l.strip()
    direction = l[0]
    amount = int(l[1:])
    if direction == "L":
      amount = -amount
    previous = current_pos
    current_pos += amount
    actual_pos = current_pos

    num_zeros = (int(abs(actual_pos) / 100))
    if actual_pos <= 0 and amount != actual_pos:
      num_zeros += 1
  
    current_pos = current_pos % 100
  
    # if current_pos == 0 and (abs(distance) % 100 != 0):
    #   num_zeros += 1
    zero_count += num_zeros    
    
    print(f"previous = {previous} | rotation = {amount} | actual = {actual_pos} | current_pos = {current_pos} | num_zeros = {num_zeros}")
  print(f"Password is {zero_count}")


def main():
  parser = argparse.ArgumentParser(prog='adventofcode day_1')
  parser.add_argument('input_file')
  parser.add_argument('--mode', default="1")
  args = parser.parse_args()

  print(f"Parsing {args.input_file}:")
  with open(args.input_file, "r") as input:
    lines = [l for l in input]
    if args.mode == "1":
      parse_input(lines)
    if args.mode == "2":
      parse_input_sophisticated(lines)


if __name__ == "__main__":
  main()
