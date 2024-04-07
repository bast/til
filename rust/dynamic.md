# How to run a Rust program as a script

Nice experimental feature available in nightly rust:
```rust
#!/usr/bin/env -S cargo +nightly -Zscript
---
[package]
edition = "2021"
[profile.dev]
opt-level = 3
[dependencies]
rand = "0.8"
---

use rand::Rng;

fn main() {
    let numbers = generate_random_points(10, 1.0);

    println!("Couple of random numbers: {:?}", numbers);
}

fn generate_random_points(num_points: usize, extent: f64) -> Vec<(f64, f64)> {
    let mut rng = rand::thread_rng();

    (0..num_points)
        .map(|_| {
            (
                rng.gen_range(-extent..extent),
                rng.gen_range(-extent..extent),
            )
        })
        .collect()
}
```

You can run this with `./hello.rs`.
