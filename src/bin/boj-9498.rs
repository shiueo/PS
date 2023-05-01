use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let num: i32 = input.trim().parse().unwrap();

    if num >= 90 {
        println!("A");
    }
    else if num >= 80 {
        println!("B");
    }
    else if num >= 70 {
        println!("C");
    }
    else if num >= 60 {
        println!("D");
    }
    else { println!("F"); }
}