let lines = In_channel.input_lines stdin

let part_one =
  let max_elf = ref ~-1 in
  let current_elf = ref ~-1 in
  List.iter
    (fun line ->
      match line with
      | "" ->
          max_elf := max !max_elf !current_elf;
          current_elf := 0
      | cal -> current_elf := !current_elf + int_of_string cal)
    lines;
  !max_elf

let part_two =
  let rec loop curr_elf elf_arr = function
    | [] -> curr_elf :: elf_arr
    | "" :: rest ->
        Format.printf "%d@." curr_elf;
        loop 0 (curr_elf :: elf_arr) rest
    | cal :: rest -> loop (curr_elf + int_of_string cal) elf_arr rest
  in
  let elf_arr = loop 0 [] lines |> List.sort (fun a b -> ~-(compare a b)) in
  List.nth elf_arr 0 + List.nth elf_arr 1 + List.nth elf_arr 2

let () =
  Format.printf "Part one: %d@." part_one;
  Format.printf "Part two: %d@." part_two
