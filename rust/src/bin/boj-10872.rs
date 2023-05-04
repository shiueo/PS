use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let n: u32 = input.trim().parse().unwrap();

    println!("{}", factorial(n));
}

pub fn factorial(num: u32) -> u32 {
    (1..=num).product()
}
