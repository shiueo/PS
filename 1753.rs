use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(Copy, Clone, Eq, PartialEq)]
struct Node {
    point: usize,
    cost: i32,
}

impl Ord for Node {
    fn cmp(&self, other: &Self) -> Ordering {
        other.cost.cmp(&self.cost)
    }
}

impl PartialOrd for Node {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

fn dijkstra(graph: &Vec<Vec<(usize, i32)>>, start_point: usize) -> Vec<i32> {
    let mut visited = vec![1e9 as i32; graph.len()];
    let mut heap = BinaryHeap::new();

    heap.push(Node { point: start_point, cost: 0 });
    visited[start_point] = 0;

    while let Some(Node { point, cost }) = heap.pop() {
        if cost > visited[point] {
            continue;
        }

        for &(i, j) in &graph[point] {
            let new_cost = cost + j;
            if new_cost < visited[i] {
                visited[i] = new_cost;
                heap.push(Node { point: i, cost: new_cost });
            }
        }
    }

    visited
}

fn main() {
    let stdin = std::io::stdin();
    let mut input_line = String::new();
    stdin.read_line(&mut input_line).unwrap();
    let mut iter = input_line.split_whitespace();
    let v: usize = iter.next().unwrap().parse().unwrap();
    let e: usize = iter.next().unwrap().parse().unwrap();

    input_line.clear();
    stdin.read_line(&mut input_line).unwrap();
    let k: usize = input_line.trim().parse().unwrap();

    let mut graph = vec![Vec::new(); v];
    for _ in 0..e {
        input_line.clear();
        stdin.read_line(&mut input_line).unwrap();
        let mut iter = input_line.split_whitespace();
        let u: usize = iter.next().unwrap().parse().unwrap();
        let v: usize = iter.next().unwrap().parse().unwrap();
        let w: i32 = iter.next().unwrap().parse().unwrap();
        graph[u - 1].push((v - 1, w));
    }

    let viz = dijkstra(&graph, k - 1);

    for i in &viz {
        if *i == 1e9 as i32 {
            println!("INF");
        } else {
            println!("{}", i);
        }
    }
}