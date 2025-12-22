let grid =
  let grid = ref (Dynarray.create ()) in
  let reading = ref true in
  while !reading do
    match read_line () with
    | exception End_of_file -> reading := false
    | line ->
        let nums =
          String.split_on_char ' ' line
          |> List.filter_map (fun elt ->
              match String.trim elt with "" -> None | _ -> Some elt)
        in
        Dynarray.add_last !grid (Dynarray.of_list nums)
  done;
  !grid

let () =
  let rows = Dynarray.length grid in
  let cols = Dynarray.length (Dynarray.get grid 0) in
  let ans = ref 0 in
  for j = 0 to cols - 1 do
    let op = String.trim (Dynarray.get (Dynarray.get_last grid) j) in
    let acc = ref (if op = "*" then 1 else 0) in
    for i = 0 to rows - 2 do
      let elt = Dynarray.get (Dynarray.get grid i) j in
      let f = if op = "*" then ( * ) else ( + ) in
      acc := f !acc (int_of_string elt)
    done;
    ans := !ans + !acc
  done;
  Format.printf "%d@." !ans
