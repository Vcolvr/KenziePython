int function() {
    int start = 1
    int end = 5
    int accumulator = 0

    While start <= end
    IF start modulo 2 ==0:
    accumulator = accumulator +start
    Else:
    accumulator = accumulator + end
    start = start +1

    return accumulator
}