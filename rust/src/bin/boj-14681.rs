use std::io;

fn main() {
    let mut input_1 = String::new();
    let mut input_2 = String::new();

    io::stdin().read_line(&mut input_1).unwrap();
    io::stdin().read_line(&mut input_2).unwrap();

    let first_num: i32 = input_1.trim().parse().unwrap();
    let second_num: i32 = input_2.trim().parse().unwrap();

    if first_num > 0 {
        if second_num > 0 {
            println!("1")
        } else {
            println!("4")
        }
    } else {
        if second_num > 0 {
            println!("2")
        } else {
            println!("3")
        }
    }
}
