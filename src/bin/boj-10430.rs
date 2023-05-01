use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let tokens:Vec<i32> = input.as_mut_str().split_ascii_whitespace().map(|input| input.parse().unwrap()).collect();

    println!("{}\n{}\n{}\n{}", (tokens[0] + tokens[1])%tokens[2], ((tokens[0]%tokens[2]) + (tokens[1]%tokens[2]))%tokens[2], (tokens[0]*tokens[1])%tokens[2], ((tokens[0]%tokens[2])*(tokens[1]%tokens[2]))%tokens[2]);
}