use std::io;

fn main() {
    let mut input_1 = String::new();

    io::stdin().read_line(&mut input_1).unwrap();

    let first_num: i32 = input_1.trim().parse().unwrap();

    for i in 1..10 {
        println!("{} * {} = {}", first_num, i, first_num * i);
    }
}
