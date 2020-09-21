(* function works as argument
Notice the type of twice is ((int -> int) * int) -> int.*)
(* use tuple as fucntion twice's argument
let twice ((f: int-> int),(x:int)): int = f (f x)
let double (x:int): int = x*2
let quad (x:int): int = twice (double, x);; works as tuple
*)
let twice (f: int-> int) (x:int): int = f (f x)
let double (x:int): int = x*2
let quad (x:int): int = twice double x;; (* two aruguments*)

print_int (quad 5);;