let joltage_part_one batteries =
  let len = String.length batteries in
  let max_joltage = ref ~-1 in
  for i = 0 to len - 1 do
    let a = Char.Ascii.digit_to_int (String.get batteries i) in
    for j = i + 1 to len - 1 do
      let b = Char.Ascii.digit_to_int (String.get batteries j) in
      let n = (a * 10) + b in
      max_joltage := max !max_joltage n
    done
  done;
  !max_joltage

let joltage_part_two batteries =
  let len = String.length batteries in
  let l, r = (ref 0, ref 12) in
  let ans = Dynarray.create () in
  while !r > 0 do
    let max_index = len - !r + 1 in
    let max_num = ref ~-1 in
    let max_i = ref ~-1 in
    for i = !l to max_index - 1 do
      let n = Char.Ascii.digit_to_int (String.get batteries i) in
      if n > !max_num then begin
        max_num := n;
        max_i := i
      end
    done;
    l := !max_i + 1;
    r := !r - 1;
    Dynarray.add_last ans !max_num
  done;
  Dynarray.to_list ans |> List.map string_of_int |> String.concat ""
  |> int_of_string

let () =
  let lines = In_channel.input_lines stdin in
  let part_one = List.map joltage_part_one lines in
  let part_two = List.map joltage_part_two lines in
  let ans_one = List.fold_left ( + ) 0 part_one in
  let ans_two = List.fold_left ( + ) 0 part_two in
  Format.printf "Part one: %d@." ans_one;
  Format.printf "Part two: %d@." ans_two
