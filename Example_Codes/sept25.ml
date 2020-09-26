
let rec prods (xs : (int * int) list) : int list = 
  match xs with
  | [] -> []
  | (x,y) :: tl -> (x*y) :: prods tl

let xs = [(2,3);(4,7);(5,2)];;
prods xs

(* zip function: if sub list are in different length, return None.
otherwise, transpose the lsit
zip [2; 3] [4; 5] == Some [(2,4); (3,5)]*)
let rec zip (xs: int list) (ys: int list) : (int * int) list option = 
  match (xs,ys) with 
  | ([], []) -> Some []
  | ([], y::ys') -> None
  | (x::xs',[]) -> None
  | (x::xs',y::ys') ->  match zip xs' ys' with
                        | Some zs -> Some((x,y)::zs)    (*the 'Some' before zs is pattern mathing the possible value*)
                        | None -> None                      (*the 'Some' before ((x,y)::zs) is key work paired with None*)


let  xs = [2;3;4]
let ys = [5;6;7];;
zip xs ys;;

let rec zip' (xs: int list) (ys: int list) : (int * int) list option = 
  match (xs,ys) with 
  | ([], []) -> Some []
  | (x::xs',y::ys') ->  (match zip xs' ys' with
                        | Some zs -> Some((x,y)::zs)    
                        | None -> None  )
  | ( _ , _) -> None ;;
                        
zip' xs ys;;



let rec insert (x: int) (xs:int list) : int list =
  match xs with
  | [] -> [x]
  | hd :: tl -> if hd < x then hd:: insert x tl
                 else x::xs

type il = int list

let insert_sort (xs : il): il = 
  let rec aux (sorted:il) (unsorted:il) = 
    match unsorted with
    | [] -> sorted
    | hd::tl -> aux (insert hd sorted) tl
  in aux [] xs 

let xs = [3;2;4;5;1];;
insert_sort(xs)