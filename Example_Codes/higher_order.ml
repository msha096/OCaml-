(* Sept 30 *)

let xs = [1;2;3;4]
let inc x = x + 1

let rec map (f: int-> int) (xs: int list) : int list = 
  match xs with
  | [] ->[]
  | hd::tl -> (f hd) :: (map f tl)

let inc_all xs = map inc xs
(* Here f is a function as input,
  Map works as a pipeline, process each element with the same function 
  We can use this way to increase all elements in the list*)


(* way 2: anonymous function*)

let inc_all' xs = map (fun x -> x + 1) xs


(* map without type
val map : ('a -> 'b) -> 'a list -> 'b list = <fun>
'a and 'b are type variables, do not have to be a specific type, but it
inidcates the relationship: if you give map a function from 'a to 'b=> 
when given a lsit of 'a values , returns a list of 'b values.

('a -> 'b) is type of function f;
'a list is the type of xs
'b list is the return type 
*)
(* can also be written in:
let rec map (f : 'a -> 'b) (xs: 'a list) : 'b list = *)
let rec map f xs = 
  match xs with
  | [] ->[]
  | hd::tl -> (f hd) :: (map f tl)

(* We say map is polymorphic in the types 'a and 'b – just a fancy
way to say map can be used on any types 'a and 'b.*)

(* map without define the type, works with the following experession
type inference will figure out the type, thus we do not need to define*)
let floats = map (fun x -> x +. 2.0) [3.1; 2.5; 4.2]

let strings = map String.uppercase_ascii ["sarah"; "joe"]
(* string->float, when given a string list, return a float list*)
let transfer = map float_of_string ["2.0";"3.2";"5.5"]

let w = map float_of_string
(* val w : string list -> float list = <fun> *)
let c = w ["1.1";"2.2"]
(*val c : float list = [1.1; 2.2] *)


