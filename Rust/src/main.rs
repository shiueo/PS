use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.trim().split_whitespace();
    let L: i32 = iter.next().unwrap().parse().unwrap();
    let P: i32 = iter.next().unwrap().parse().unwrap();

    let mut news_input = String::new();
    io::stdin().read_line(&mut news_input).unwrap();
    let news: Vec<i32> = news_input
        .trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    for i in news {
        print!("{} ", i - L * P);
    }
}
