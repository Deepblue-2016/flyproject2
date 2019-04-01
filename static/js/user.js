sum = 0;

function humancheck1() {
    var s1 = Math.ceil(Math.random() * 5);
    var s2 = Math.ceil(Math.random() * 5);

    sum = s1 + s2;

    var obj = document.getElementById('humancheck');

    obj.innerHTML = s1 + '+' + s2 + '= ?';
}

function humancheck2() {
    L_vercode = document.getElementById('L_vercode');

    console.log(L_vercode.value);

    if (sum == L_vercode.value) {
        var obj = document.getElementById('humancheck');
        obj.innerHTML = '来了老弟！';
    } else {
        var obj = document.getElementById('humancheck');
        obj.innerHTML = 'are u ok ?';
    }

}