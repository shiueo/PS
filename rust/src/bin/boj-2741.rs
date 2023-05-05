use std::fmt::Write;
use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();

    let n: i32 = input.trim().parse().unwrap();

    let mut output = String::new();
    for i in 1..n + 1 {
        writeln!(output, "{}", i).unwrap();
    }
    print!("{}", output);
}
