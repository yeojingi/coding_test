const { rawListeners } = require('process');

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let inputs = [];
let T = -1, c = -1;

readline.on('line', function(line) {
    if (T === -1) {
        T = parseInt(line);
        c = T* 2;
    } else if (c > 0) {
        if ( c%2 == 1) {
            inputs.push( line.split(' ').map(el => parseInt(el)));
        } else {
        }
        c--;
    }
    
    if (c == 0) {
        readline.close();
    }
}).on('close', function(){ //이 안에 솔루션 코드 작성
    solution(inputs);
    process.exit();
});

const solution = inputs => {
    let anss = [];

    for (let input of inputs) {
        let ans = 0;
        input.sort((a,b ) => b-a);
        

        for (let i = 0; i < input.length-2; i ++) {
            ans = Math.max(ans, input[i] - input[i+1], input[i] - input[i+2])
        }
        ans = Math.max(ans, input[input.length-2] - input[input.length-1])

        console.log(ans)
    }

    // console.log(anss);
};