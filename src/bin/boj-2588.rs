use std::io;

fn main() {
    let mut input_1 = String::new();
    let mut input_2 = String::new();

    io::stdin().read_line(&mut input_1).unwrap();
    io::stdin().read_line(&mut input_2).unwrap();

    let first_num: i32 = input_1.trim().parse().unwrap();
    let second_num: i32 = input_2.trim().parse().unwrap();

    let number_vec = vec![second_num % 10, (second_num % 100) / 10, (second_num) / 100];

    for i in number_vec.iter() {
        println!("{}", first_num * i);
    }

    println!("{} ", first_num * second_num);
}