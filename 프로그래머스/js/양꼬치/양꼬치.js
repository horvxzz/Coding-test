function solution(n, k) {
    var freeDrinks = Math.floor(n / 10);
    var payableDrinks = Math.max(k - freeDrinks, 0);
    var answer = n * 12000 + payableDrinks * 2000;
    return answer;
}
