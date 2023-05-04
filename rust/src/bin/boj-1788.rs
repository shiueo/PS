use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut n: i32 = input.trim().parse().unwrap();

    let mut fibonacci: Vec<i32> = vec![0, 1];
    if n > 0 {
        for i in 1..n as usize {
            fibonacci.push((fibonacci[i] + fibonacci[i - 1]) % 1000000000);
        }
        n = fibonacci[fibonacci.len() - 1];
    } else if n == 0 {
        fibonacci.pop();
    } else {
        n = n.abs();
        for i in 1..n as usize {
            fibonacci.push((fibonacci[i] + fibonacci[i - 1]) % 1000000000);
        }
        if n % 2 == 0 {
            n = -1 * fibonacci[fibonacci.len() - 1];
        } else {
            n = fibonacci[fibonacci.len() - 1];
        }
    }

    if n > 0 {
        println!("1");
    } else if n == 0 {
        println!("0");
    } else {
        println!("-1");
    }
    println!("{}", n.abs());
}
