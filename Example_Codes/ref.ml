
let c = ref 0 in 
 let x = !c in 
  c := 42;
  print_string " x:";
  print_int x;  (* x is 0, and x is immutable*)
  let y = !c in 
   print_string " y:";
   print_int y;; (* y is 42*)
  
let c = ref 0

let next () =
  let v = !c in   (* v is immutable*)
   (c := v+1 ; v)    (* when e1:unit, and e2:t, then (e1;e2):t*)
(* to write t:= 5   returns nothing  - : unit = () *)
(* this function do the operation and return the value of v*)
;;
next () ;;
c;;
next () ;;
c;;

let next' () =
  let v = !c in
  let _ = c := v+1 in
  v
;;
next' ();;
c;; (* c is modified even in let..in experssion*)




let counter () =
  let k = ref 0 in
  fun () ->
    let v = !k in
      (k := v+1 ; v)
;;
print_string "here";;
let countA = counter () 
let countB = counter () ;;
countA () ;;
countA () ;;
countB () ;;
countB () ;;
countA () ;;
countA == countB;; (* - : bool = false *)

print_string "here...in";;
let countA = counter() in
 let countB = counter() in
  countA() ; (* 0 *)
  countA() ; (* 1 *)
  countB() ; (* 0 *)
  countB() ; (* 1 *)
  countA() ;; (* 2 *)
(* returns 2, let .. in  function only return the last line's result*)
print_string "call function";;
counter() ();;
counter() ();;
counter() ();;
counter() == counter();; (* - : bool = false, id are different *)
(* 
- : int = 0
- : int = 0
- : int = 0
counter () ;;
- : unit -> int = <fun>
*)


(*
let d1 = 3 in
 let d2 = 5 in
  let m = d1 * d2 in
   let a = d1 + d2 in
    print_int m;
    print_endline "";
    print_int a; 


let p a = 
  a + 2;
  print_int a ;;
  
p 4;; 
*)
 
 
let c = ref 0;;
let x = c ;;
x := 42 ;;
!c ;; (* - : int = 42 *)


let l = [2;3;4;5;6]

let f1 (l: int list) : unit = 
 match l with
 | _ :: tl -> print_int (List.length tl)
 | [] -> print_int 0
;;
f1 l;;
