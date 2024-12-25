// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "AdventOfCode",
    platforms: [
        .macOS(.v13)
    ],
    dependencies: [
         .package(url: "https://github.com/mtynior/ColorizeSwift.git", from: "1.7.0"),
    ],
    targets: [
        .executableTarget(
            name: "Day5",
            dependencies: ["ColorizeSwift"]
        ),
        .testTarget(
            name: "Day5Tests", 
            dependencies: ["Day5"]
        )
    ]
)
