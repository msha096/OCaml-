exception Signal of int
exception Ovflw
;;
raise Ovflw;;
let x = 2;;
raise (Signal (x+4));;

let f (x:int) = 
  if x < 1 then raise Ovflw
  else 1/x;;


(try f 0 with| Ovflw -> 0)/(try f x with| Ovflw -> 1)


let g x = 
  if x=0 then raise (Signal 0)
  else if x=1 then raise (Signal 1)
  else if x=10 then raise (Signal (x-8))
  else (x-2) mod 4;;
try g 10 with | Signal 0 -> 0
| Signal 1 -> 1
| Signal x -> x+8


type ('v) tree = Leaf of int| Node of ('v) tree * ('v) tree
let test = Leaf 0;;
let exception Zero in
  let rec prod (t: 'v tree) : int =
  match t with
  | Leaf x -> if x=0 then (raise Zero) else x
  | Node (x,y) -> (prod x) * (prod y)
 in
  try (prod test) with Zero -> (print_int 0;0)