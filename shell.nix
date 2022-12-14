{ nixpkgs ? import <nixpkgs> {  } }:

let
  pkgs = [
    nixpkgs.ripgrep
    nixpkgs.python3
    nixpkgs.python3.pkgs.pylint
    nixpkgs.python3.pkgs.jedi
    nixpkgs.python3.pkgs.numpy
  ];
 
in
  nixpkgs.stdenv.mkDerivation {
    name = "AoC";
    buildInputs = pkgs;
  }
