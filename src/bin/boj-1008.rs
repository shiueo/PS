use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let tokens:Vec<f64> = input.as_mut_str().split_ascii_whitespace().map(|input| input.parse().unwrap()).collect();

    println!("{:.20}", tokens[0] / tokens[1]);
}