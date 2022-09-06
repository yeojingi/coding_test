const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
let N= undefined;
let count = 0;

readline.on('line', function(line) {
  if (N === undefined) {
    N = parseInt(line);
    count = N;
  }
  else {
    inputs.push(line.split(' ').map(el => parseInt(el)))
    count--;
    if (count === 0) {
      readline.close();
    }
  }
}).on('close', function(){ //이 안에 솔루션 코드 작성
  solution(inputs);
  process.exit();
});

const solution = (inputs) => {
  const cmp = (a,b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  };
  inputs.sort(cmp)

  let A = inputs.map((v) => v.join(" ")).join("\n");
  console.log(A)
};