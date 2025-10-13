<h4>

정수 `n`과 정수 배열 `numlist`가 매개변수로 주어질 때, `numlist`에서 `n`의 배수가 아닌 수들을 제거한 배열을 `return`하도록 `solution` 함수를 완성해주세요.

</h4>

---

<br>

`n`의 배수가 아닌 수들을 제거한 배열을 저장할 새로운 배열을 선언해 준다<br>
for 문으로 `numlist`에 들어있는 원소들을 전체 검사한다<br>
if문으로 만약 `i`가 `n`의 배수라면 새로운 배열인 `newlist`에 `append`를 이용해 추가해준다<br>
`newlist`를 반환한다<br>