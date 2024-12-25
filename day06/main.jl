using Printf

global testinput = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

struct LoopError <: Exception 
    msg::String
end

function parse(input)
    return reduce(vcat, permutedims.(collect.(split(strip(input), '\n'))))
end

function part1(grid)
    guardPosition = [0,0]
    guardDirection = "north"
    # i is row index, j is column index
    for i = 1:grid.size[1]
        for j = 1:grid.size[2]
            if grid[i,j] == '^'
                guardPosition = [i,j]
            end
        end
    end
    @assert guardPosition != [0,0]
    seenstates = Set{Tuple{Array{Int},String}}()
    

    # Move guard according to rules
    while true
        grid[guardPosition[1], guardPosition[2]] = 'X'
        if guardDirection == "north"
            if guardPosition[1] > 1 
                if grid[guardPosition[1]-1,guardPosition[2]] != '#'
                    guardPosition[1] = guardPosition[1] - 1
                else 
                    guardDirection = "east"
                end
            else
                break
            end
        elseif guardDirection == "east"
            if guardPosition[2] < grid.size[2]
                if grid[guardPosition[1],guardPosition[2]+1] != '#'
                    guardPosition[2] = guardPosition[2] + 1
                else 
                    guardDirection = "south"
                end
            else
                break
            end
        elseif guardDirection == "south"
            if guardPosition[1] < grid.size[1] 
                if grid[guardPosition[1]+1,guardPosition[2]] != '#'
                    guardPosition[1] = guardPosition[1] + 1
                else 
                    guardDirection = "west"
                end
            else
                break
            end
        elseif guardDirection == "west"
            if guardPosition[2] > 1
                if grid[guardPosition[1],guardPosition[2]-1] != '#'
                    guardPosition[2] = guardPosition[2] - 1
                else 
                    guardDirection = "north"
                end
            else
                break
            end
        end
        if in!((copy(guardPosition), guardDirection), seenstates)
            throw(LoopError("guard stuck in a loop"))
            return -1
        end
    end
    
    count(==('X'), grid)
end

function part2(grid)
    count = 0
    for i = 1:grid.size[1]
        @printf("Checking line (%d/%d)\r", i, grid.size[1])
        for j = 1:grid.size[2]
            if grid[i,j] == '.'
              
                newgrid = copy(grid)
                newgrid[i,j] = '#'
                try
                    part1(newgrid) == -1
                catch e
                    if e isa LoopError
                        count += 1
                    end
                end
            end
        end
        flush(stdout)
    end
    println()
    count
end

open("day06/input", "r") do file
    grid = parse(read(file, String))
    @printf("Test: Expected 41, got: %d\n", part1(parse(testinput)))
    @printf("Solution: %d\n\n", part1(copy(grid)))
    @printf("Test: Expected 6, got: %d\n", part2(parse(testinput)))
    @printf("Solution: %d\n", part2(copy(grid)))
end