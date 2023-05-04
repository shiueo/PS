use std::io;

fn main() {
    let mut input_1 = String::new();
    io::stdin().read_line(&mut input_1).unwrap();
    let first_num: i32 = input_1.trim().parse().unwrap();

    if first_num % 400 == 0 {
        println!("1")
    } else if first_num % 100 == 0 {
        println!("0")
    } else if first_num % 4 == 0 {
        println!("1")
    } else {
        println!("0")
    }
}
