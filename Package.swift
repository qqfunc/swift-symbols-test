// swift-tools-version: 6.2

import PackageDescription

let package = Package(
    name: "swift-symbols",
    products: [.library(name: "Symbols", targets: ["Symbols"])],
    targets: [
        .target(name: "Symbols"),
        .testTarget(name: "SymbolsTests", dependencies: ["Symbols"]),
    ]
)
