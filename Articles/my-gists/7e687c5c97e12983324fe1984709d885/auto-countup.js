// 入力フィールドの要素を取得
const inputField = document.querySelector('#quiz-answer');

// カウンターの初期値を設定
let counter = 1;

// クリックイベントのリスナーを追加
const submitButton = document.querySelector('#submit-quiz-answer');
submitButton.addEventListener('click', () => {
  // 入力フィールドを空にする
  inputField.value = '';

  // 入力フィールドに現在のカウンターの値を設定
  inputField.value = counter.toString();

  // カウンターをインクリメント
  counter++;

  // カウンターが1001になったら終了
  if (counter === 1001) {
    console.log('終了しました。');
  }
});