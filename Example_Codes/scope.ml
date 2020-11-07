(*Pseudo-code:
function f (x) =
{ x := x+1; return x };
var y : int = 0;
f(y)+y; *)


(* pass-by-reference *)
let f (x : int ref) =
  ( x := !x+1; !x ) in
  let y = ref 0 in
  let z = f(y) in
  z + !y


(* pass-by-value *)
let f (w : int) =
  (let x = ref w in
  x := !x+1; !x) in
  let y = ref 0 in
  let z = f(!y) in
  z + !y

  (* z + !y yield different results*)



let x = 1 in
 let g z = x + z in
  let f y =
   (let x = y + 1 in
    g (y*x)) in
  f 3
(* g(12) x+z which x is used?*)
(* dynamic scope: x = 4 *)
(* static scope: x = 1 *)