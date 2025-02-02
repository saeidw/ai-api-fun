{ pkgs ? import <nixpkgs> {}
, compiler ? "ghc965"
}:

let
  ghc = pkgs.haskell.packages.${compiler}.ghcWithPackages (_: []);
in
  pkgs.stdenv.mkDerivation {
    name = "ai-data-fun-dev";
    buildInputs = [
      ghc
      pkgs.zlib
      pkgs.python3
      pkgs.cabal-install
      pkgs.openssl
      pkgs.haskellPackages.hspec-discover
      pkgs.haskellPackages.haskell-language-server
      pkgs.haskellPackages.ormolu
      pkgs.haskellPackages.hlint
      pkgs.pkg-config
      pkgs.sqlite
      pkgs.python3
      pkgs.python3Packages.pip
      pkgs.python3Packages.sqlalchemy
      pkgs.python3Packages.fastapi
      pkgs.python3Packages.uvicorn
      pkgs.python3Packages.python-lsp-server
      pkgs.pylint
    ];
    shellHook = ''
      eval $(grep export ${ghc}/bin/ghc)
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"${pkgs.zlib}/lib";
    '';
  }