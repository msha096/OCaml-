(* example signature*)
module type INT_STACK = 
 sig
  type t
  val empty : unit -> t
  val push : int -> t -> t
  val is_empty : t -> bool
  val pop : t -> t
  val top : t -> int option
 end

 (* use empty like : empty ()  to get an empty stack*)
 (* empty and push are abstract constructor*)
 (* is_empty and top are observers, they do not change the stack*)
 (* pop is mutator*)

(* example structure*)
module ListIntStack : INT_STACK = 
  struct 
    type t = int list
    let empty () : t = []
    let push (i:int) (s:t) : t = i ::s (* add the element to the first place*)
    let is_empty (s:t) = 
      match s with
      | [] -> true
      | _::_ -> false
    let pop (s:t) : t = 
      match s with
      | [] -> []
      | _ :: tl -> tl (* return the stack without the first element*)
    let top (s:t) : int option = 
      match s with
      | [] -> None
      | h::_ -> Some h (* return the first element in the stack*) 
  end



let s0 = ListIntStack.empty ()
let s1 = ListIntStack.push 3 s0
let s2 = ListIntStack.push 4 s1
let s3 = ListIntStack.push 5 s2
let t = ListIntStack.top s3
(* val t : int option = Some 5 *)
let i = ListIntStack.top s2
(* i : int option = Some 4 *)
let j = ListIntStack.top (ListIntStack.pop s2)
(* j : int option = Some 3 *)

(* NOTICE: the abstract data is highly sealed, the client can not use ListIntStack as a list.Bigarray
E.g., let l = List.rev s2 will raise an error*)


(* A signature for Polymorphic stacks*)
module type STACK = 
 sig 
  type 'a stack
  val empty : unit -> 'a stack
  val push : 'a -> 'a stack -> 'a stack
  val is_empty : 'a stack -> bool
  val pop : 'a stack -> 'a stack
  val top : 'a stack -> 'a option 
 end

module ListStack : STACK = 
 struct
  type 'a stack = 'a list
  let empty () : 'a stack = []
  let push (x:'a) (s:'a stack) : 'a stack = x::s
  let is_empty (s:'a stack): bool = 
    match s with
    | [] -> true
    | _::_ ->  false
  let pop (s:'a stack) : 'a stack =
    match s with
    | [] -> []
    | _::tl -> tl
  let top (s:'a stack) : 'a option = 
    match s with
    | [] -> None
    | h::_ -> Some h
  end



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
  let empty () : 'a stack = ref []
  let push (x:'a) (s:'a stack) : unit =
   s := x::(!s)
  let pop (s:'a stack) : 'a option =
   match !s with
   | [] -> None
   | h::t -> (s := t ; Some h)
  end