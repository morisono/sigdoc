// 入力フィールドの要素を取得
const inputField = document.querySelector('#quiz-answer');

// カウンターの初期値を設定
let counter = 0;

// クリックイベントのリスナーを追加
const submitButton = document.querySelector('#submit-quiz-answer');
submitButton.addEventListener('click', () => {
  // 入力フィールドを空にする
  inputField.value = '';

  // 入力された値を数値に変換してステップ数として扱う
  const step = parseInt(inputField.value);

  // 最初に入力された値が0の場合はZero padしない
  const shouldZeroPad = counter === 0;

  // ゼロパディングの判定
  inputField.value = shouldZeroPad ? counter.toString().padStart(3, '0') : counter.toString();

  // カウンターにステップ数を加算
  counter += step;

  // カウンターが1001以上になったら終了
  if (counter >= 1001) {
    console.log('終了しました。');
  }
});
