// 入力フィールドと確認ボタンの要素を取得
const inputField = document.querySelector('#quiz-answer');
const submitButton = document.querySelector('#submit-quiz-answer');

// カウンターの初期値を設定
let counter = 1;

// 入力と確認ボタンのクリックを行う関数
async function inputAndClick() {
  // 入力フィールドを空にする
  inputField.value = '';

  // 入力フィールドに現在のカウンターの値を設定
  inputField.value = counter.toString();

  // 確認ボタンをクリック
  submitButton.click();

  // カウンターをインクリメント
  counter++;

  // カウンターが1001になったら終了
  if (counter === 1001) {
    console.log('終了しました。');
    return;
  }

  // 次の入力とクリックを行う
  setTimeout(inputAndClick, 100);
}

// 処理を遅延して開始
window.addEventListener('load', () => {
  setTimeout(inputAndClick, 100);
});