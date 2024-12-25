import Foundation

import ColorizeSwift

struct PuzzleData {
    var rules: [Int:[Int]] = [:]
    var updates: [[Int]] = []
}

func parse(_ input: String) -> PuzzleData {
    var data = PuzzleData()
    let ruleRegex: Regex = #/(\d+).(\d+)/#
    let updateRegex: Regex = #/\d+(?:,\d+)*/#

    for line in input.split(separator: "\n") {
        if let ruleMatch = try? ruleRegex.wholeMatch(in: line) {
            let left = Int(ruleMatch.1)!
            let right = Int(ruleMatch.output.2)!
            if  data.rules.keys.contains(right) {
                data.rules[right]!.append(left)
            } else {
                data.rules[right] = [left]
            }
        }
        if (try? updateRegex.wholeMatch(in: line)) != nil {
            data.updates.append(line.split(separator: ",").map({Int((try! #/\d+/#.wholeMatch(in: $0)!).0)!}))
        }
    }
    return data
}

func isOrderedCorrectly(_ update: [Int], rules: [Int:[Int]]) -> Bool {
    var alreadyPrinted = Set<Int>()
    for page in update {
        for dependency in rules[page] ?? [] {
            if update.contains(dependency) && !alreadyPrinted.contains(dependency) {
                return false
            }
        }
        alreadyPrinted.insert(page)
    }
    return true
}

public func part1(_ input: String) -> Int {
    let puzzleData = parse(input)
    var result = 0
    for update in puzzleData.updates {
        if isOrderedCorrectly(update, rules: puzzleData.rules) {
            result += update[update.count / 2]
        }
    }
    return result
}

public func part2(_ input: String) -> Int {
    let puzzleData = parse(input)
    var result = 0
    for update in puzzleData.updates {
        if !isOrderedCorrectly(update, rules: puzzleData.rules) {
            let orderedUpdate = update.sorted(by: { (puzzleData.rules[$1] ?? []).contains($0) && !(puzzleData.rules[$0] ?? []).contains($1) })
            assert(orderedUpdate.count == update.count)
            assert(isOrderedCorrectly(orderedUpdate, rules: puzzleData.rules))
            result += orderedUpdate[orderedUpdate.count / 2]
        }
    }
    return result
}

print("Part 1".bold())
try! print("Solution \(part1(String(contentsOf: URL(string: "../../input", relativeTo: URL(filePath: #filePath))!, encoding: .utf8)))")
print()
print("Part 2".bold())
try! print("Solution \(part2(String(contentsOf: URL(string: "../../input", relativeTo: URL(filePath: #filePath))!, encoding: .utf8)))")
