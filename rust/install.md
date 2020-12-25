Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  /Users/spark/.rustup



This can be modified with the RUSTUP_HOME environment variable.

The Cargo home directory located at:

  /Users/spark/.cargo

This can be modified with the CARGO_HOME environment variable.

The cargo, rustc, rustup and other commands will be added to
Cargo's bin directory, located at:

  /Users/spark/.cargo/bin

This path will then be added to your PATH environment variable by
modifying the profile files located at:



/Users/spark/.profile
  /Users/spark/.bash_profile
  /Users/spark/.bashrc
  /Users/spark/.zshenv

You can uninstall at any time with rustup self uninstall and
these changes will be reverted.



Rust is installed now. Great!

To get started you need Cargo's bin directory ($HOME/.cargo/bin) in your PATH
environment variable. Next time you log in this will be done
automatically.

To configure your current shell, run:
source $HOME/.cargo/env