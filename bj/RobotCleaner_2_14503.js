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
    if (rows[r][c] == 0) {
      ans ++;
      rows[r][c] = ans;

    }
    backIsWall = false;
    for (let i = 0; i < 5; i++) {
      let nd = (d + i) % 4;
      let nr = r + dr[nd];
      let nc = c + dc[nd];

      if (rows[nr][nc] == 0) {
        d = nd;
        r = nr;
        c = nc;
        break;
      }

      if (i == 2) {
        if (rows[nr][nc] == 1) {
          backIsWall = true;
        }
      }

      if (i == 4) {
        if (backIsWall) {
          conti = false;
          break;
        }
        else {
          nd = (d + 2) % 4;
          nr = r + dr[nd];
          nc = c + dc[nd];
          r = nr;
          c = nc;
          break;
        }
      }
    }
  }

  console.log('---')
  for (const row of rows) {
    console.log(row.join(' '))
  }
  console.log(ans);
};