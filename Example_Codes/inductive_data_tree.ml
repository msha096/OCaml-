type key = int
type value = string
type tree = Leaf | Node of key * value * tree * tree
(* Node 9 "a" (Node 3 "b"....)*)
let rec insert (t:tree) (k:key) (v:value) :tree = 
  match t with
  | Leaf -> Node (k, v, Leaf, Leaf)
  | Node ( k', v', left, right) ->
      if k < k' then Node (k', v', insert left k v,right)
      else if k > k' then Node ( k', v', left, insert right k v)
      else Node (k,v,left,right) (* k = k', means it already in the tree*)


let t = Node (9,"a", Node(3,"b",Leaf, Node(7,"d",Leaf,Leaf)),Node(12,"c",Leaf,Leaf));;
let t1 = insert t 0 "z"
let t2 = insert t1 19 "x"


type ('key, 'value) tree = Leaf | Node of 'key * 'value * ('key, 'value) tree * ('key, 'value) tree
(* key and value can be any type*)
type 'a inttree = (int, 'a) tree
(* key is int, value can be any type*)
type stree = string inttree
(* stree is int* string type*)
