use std::cmp;
use std::io;

fn main() {
    let buf = io::read_to_string(io::stdin()).unwrap();
    let input = buf.split_ascii_whitespace().flat_map(str::parse::<i32>);

    let arr: Vec<_> = input.skip(1).collect();

    let mut v_arr = vec![arr[0]];
    let mut max_v: i32 = -1000;

    for i in 1..arr.len() {
        let v = arr[i].max(arr[i] + v_arr[i - 1]);
        v_arr.push(v);
        max_v = cmp::max(max_v, v)
    }
    println!("{}", v_arr.iter().max().unwrap());
}
