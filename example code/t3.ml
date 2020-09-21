(* function works as argument
Notice the type of twice is ((int -> int) * int) -> int.*)
let twice ((f: int-> int),(x:int)): int = f (f x)
let double (x:int): int = x*2
let quad (x:int): int = twice (double,x);;

print_int (quad 5);;