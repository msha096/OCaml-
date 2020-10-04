(* Sept 30 *)
type point = float * float  (* type abbreviation *)
type my_bool = Tru | Fal (* type defination *)
type color = Blue | Yellow | Green | Red

(* they can be used as option*)

let b1 : my_bool = Tru (* use constructors to creat values *)
let c1 : color = Yellow


let print_color (c:color) : unit = 
  match c with
  | Blue -> print_string "blue"
  | Yellow -> print_string "Yellow"
  | _ -> print_string "other"

type simple_shape = Circle of point * float | Square of point * float
(* of is a keyword
A of b, means... type name A, and A is in b type*)
let origin : point = (0.0, 0.0) 
let cir1 : simple_shape = Circle (origin, 1.0)
let sq1 : simple_shape = Square (origin, 2.0)
let cir2 : simple_shape = Circle ((1.1, 2.2), 2.0)

let simple_area (s:simple_shape) : float = 
  match s with
  | Circle (_, radius) -> 3.14 *. radius *. radius
  | Square (_, side) -> side *. side


type point = float * float
type radius = float
type side = float

let pi = 3.14

type shape = Square of side | Ellipse of radius * radius | RtTriangle of side * side| Polygon of point list
let sq : shape = Square 2.
let ell : shape = Ellipse (1.0, 2.0)
let rt : shape = RtTriangle (1.0, 1.0)
let poly ： shape = Polygon [(0.,0.);(1.,0.);(0., 1.)]

let tri_area (p1: point) (p2:point) (p3:point): float = 
  2.(* we skipped some calculation*)

let rec poly_area (ps : point list) : float = 
  match ps with 
  | p1 :: p2 :: p3 :: tail -> tri_area p1 p2 p3 +. poly_area ( p1::p3::tail)
  | _ -> 0.             (* indicating has at least three elements*)

let area (s: shape) : float =  
  match s with
  | Square s -> s *. s
  | Ellipse (r1,r2) -> pi *. r1 *. r2
  | RtTriangle (s1,s2) -> s1 *. s2 /. 2.
  | Polygon ps -> poly_area ps

