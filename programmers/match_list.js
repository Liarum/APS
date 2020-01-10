// Programmers pb.예상대진표

function rangeCheck(a, b, m)
{
    let S = 1;
    let D = 2 ** m;
    let E = D;
    let aIdx = -1;
    let bIdx = -1;

    while (aIdx===-1 || bIdx===-1) {
        if (S <= a && a <= E) {
            aIdx = S;
        }
        if (S <= b && b <= E) {
            bIdx = S;
        }
        S = E + 1;
        E = E + D;
    }
    if (aIdx===bIdx) {
        return true;
    } return false;
}
function solution(n,a,b)
{
    let m = 1;
    while (true) {
        if (rangeCheck(a, b, m)) {
            return m;
        } m++;
    }
}

console.log(solution(16, 1, 5));