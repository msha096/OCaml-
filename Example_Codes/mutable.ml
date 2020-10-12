(* imperative stack, with mutable ref*)

module type IMP_STACK =
 sig
 type 'a stack
 val empty : unit -> 'a stack
 val push : 'a -> 'a stack -> unit
 val pop : 'a stack -> 'a option
 end

module ImpStack : IMP_STACK =
  struct
  type 'a stack = ('a list) ref  
  (* The list is an immutable data structure stored 
  in a single mutable cell*)
  let empty () : 'a stack = ref []
  let push (x:'a) (s:'a stack) : unit =
   s := x::(!s)
  let pop (s:'a stack) : 'a option =
   match !s with
   | [] -> None
   | h::t -> (s := t ; Some h)
  end


(* fully mutable list*)

type 'a mlist = Nil | Cons of 'a * ('a mlist ref)
let ml = Cons(1, ref (Cons(2, ref(Cons(3, ref Nil)))))
let ml2 = Cons(7, ref Nil)



let rec fudge (l:'a mlist) (m: 'a mlist) : unit = 
   match l with
   | Nil -> ()
   | Cons(h,t) -> t:= m; ()
;;
fudge ml ml2;;
ml;; 
(* - : int mlist = Cons (1, {contents = Cons (7, {contents = Nil})})*)

let rec mlength ( m: 'a mlist) : int = 
  match m with
  | Nil -> 0
  | Cons(h,t) -> 1 + mlength(!t) 
;;
mlength ml;;

(*
let r = ref Nil in 
 let m = Cons (3,r) in
  (r := m; mlength m)
*)
(* Stack overflow during evaluation (looping recursion?)*)


(* concatenating two list, which is mutable append*)
let rec mappend xs ys =
  match xs with
  | Nil -> ()
  | Cons(h,t) -> 
       (match !t with
       | Nil -> t:=ys
       |Cons(_,_) as m -> mappend m ys
       ) (* m is !t*)

let x = Cons(1,ref (Cons (2, ref (Cons (3, ref Nil))))) ;;
let y = Cons(4,ref (Cons (5, ref (Cons (6, ref Nil))))) ;;
mappend x y ;;
x;;
