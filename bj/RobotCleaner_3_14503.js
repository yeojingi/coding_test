const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let inputs = [];
let N, M = undefined;
let r, c, d = undefined;
let count = 0, e = true;

readline.on('line', function(line) {
  if (N === undefined) {
    [N, M] = line.split(' ').map(el => parseInt(el));
    count = N;
  } else {
    if ( e ) {
      [r, c, d] = line.split(' ').map(el => parseInt(el));
      e = false;
      return; 
    }
    if (count>0) {
      inputs.push(line.split(' ').map(el => parseInt(el)))
      count --;
    } 
    if (count === 0) {
      readline.close();
    }
  }
}).on('close', function(){ //이 안에 솔루션 코드 작성
    solution(r, c, d, inputs);
    process.exit();
});

const solution = (r, c, d, rows) => {
  let ans = 0, conti = true, backIsWall = false;
  let dr = [-1, 0, 1, 0];
  let dc = [0, 1, 0, -1];
  
  while (conti) {
    let cantMove = true;
    if (rows[r][c] == 0) {
      ans ++;
      rows[r][c] = ans+10;
    }

    for (let i = 0 ; i < 4; i++) {
      let nd = (d + i * 3) % 4;
      let nr = r + dr[nd];
      let nc = c + dc[nd];

      if (rows[nr][nc] === 0) {
        cantMove = false;
        break;
      }
    }

    if (cantMove) {
      let bd = (d + 2) % 4;
      let nr = r + dr[bd];
      let nc = c + dc[bd];

      if (rows[nr][nc] === 1) {
        break;
      } else {
        r = nr;
        c = nc;
        continue;
      }
    }

    for (let i = 1; i < 5; i ++) {
      let nd = (d+i*3)%4;
      let nr = r + dr[nd];
      let nc = c + dc[nd];
      
      if (rows[nr][nc] === 0) {
        d = nd;
        r = nr;
        c = nc;
        break;
      }
    }
  }

  // console.log('---')
  // for (const row of rows) {
  //   console.log(row.join(' '))
  // }
  console.log(ans);
};