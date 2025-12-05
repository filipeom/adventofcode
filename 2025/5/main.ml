let ranges, dates =
  let ranges = ref [] in
  let dates = ref [] in
  let can_read = ref true in
  while !can_read do
    match read_line () with
    | "" -> can_read := false
    | line ->
        let range = String.split_on_char '-' line in
        let low = int_of_string @@ List.nth range 0 in
        let high = int_of_string @@ List.nth range 1 in
        assert (low <= high);
        ranges := (low, high) :: !ranges
  done;
  can_read := true;
  while !can_read do
    match read_line () with
    | exception End_of_file -> can_read := false
    | line -> dates := int_of_string line :: !dates
  done;
  (!ranges, !dates)

let () =
  let ans = ref 0 in
  List.iter
    (fun d ->
      if List.exists (fun (low, high) -> d >= low && d <= high) ranges then
        incr ans)
    dates;
  Format.printf "Part one: %d@." !ans

let union ranges =
  let sorted_ranges =
    List.sort
      (fun (l1, h1) (l2, h2) ->
        let cmp = compare l1 l2 in
        if cmp = 0 then compare h1 h2 else cmp)
      ranges
  in
  let rec merge acc = function
    | [] -> acc
    | ((l_curr, h_curr) as current) :: rest -> (
        match acc with
        | [] -> merge (current :: acc) rest
        | (l_acc, h_acc) :: rest_acc ->
            if l_curr <= h_acc + 1 then
              merge ((l_acc, max h_curr h_acc) :: rest_acc) rest
            else merge (current :: acc) rest)
  in
  merge [] sorted_ranges

let () =
  let merged_ranges = union ranges in
  let ans =
    List.fold_left
      (fun acc (l, h) ->
        (* Format.printf "%d-%d@." l h; *)
        acc + (h - l + 1))
      0 merged_ranges
  in
  Format.printf "Part two: %d@." ans
