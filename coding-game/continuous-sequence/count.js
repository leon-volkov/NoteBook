const n = parseInt(readline());
var inputs = readline().split(' ');
let current = [];
let max = [];
for (let i = 0; i < n; i++) {
    const x = parseInt(inputs[i]);

    if (current.length === 0 || current[current.length - 1] + 1 === x) {
        current.push(x);
    } else {
        if (current.length > max.length) {
            max = current;
        }

        current = [x];
    }
}

if (current.length > max.length) {
    max = current;
}

print(max[0] + ' ' + max[max.length - 1]);

//

const n = parseInt(readline());
var a = readline().split(' ').map(z => +z);
os=[[a[0],a[0]]];
for (let i = 1; i < n; i++) {
    last = os[os.length-1];
    if(last[1] + 1 == a[i]) {
        last[1] = a[i];
    } else {
        os.push([a[i], a[i]]);
    }
}
printErr(os)
o=os[0];
for(i = 1; i < os.length; i++) {
    if(os[i][1] - os[i][0] > o[1] - o[0]) o = os[i];
}

console.log(...o);
