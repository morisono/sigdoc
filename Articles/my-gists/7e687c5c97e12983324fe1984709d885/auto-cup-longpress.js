// 入力フィールドの要素を取得
const inputField = document.querySelector('#quiz-answer');

// カウンターの初期値を設定
let counter = 1;
let intervalId; // インターバルIDを格納する変数
let isMouseDown = false; // マウスが押されているかどうかを示すフラグ

// submitButtonのmousedownイベントのリスナーを追加
const submitButton = document.querySelector('#submit-quiz-answer');
submitButton.addEventListener('mousedown', () => {
  isMouseDown = true; // マウスが押されたことを示すフラグを設定
  // インクリメント
  incrementCounter();
  // 1秒後に連続インクリメントを開始
  setTimeout(() => {
    if (isMouseDown) {
      intervalId = setInterval(incrementCounter, 100); // 100msごとに実行
    }
  }, 1000); // 長押し開始から1秒後に実行
});

// submitButtonのmouseupイベントのリスナーを追加
submitButton.addEventListener('mouseup', () => {
  isMouseDown = false; // マウスが離されたことを示すフラグを設定
  // ボタンから指が離れたときにインターバルをクリア
  clearInterval(intervalId);
});

// submitButtonのmouseoutイベントのリスナーを追加
submitButton.addEventListener('mouseout', () => {
  isMouseDown = false; // マウスが離れたことを示すフラグを設定
  // マウスがボタンの外に移動したときにインターバルをクリア
  clearInterval(intervalId);
});

// カウンターをインクリメントする関数
function incrementCounter() {
  // 入力フィールドを空にする
  inputField.value = '';
  // 入力フィールドに現在のカウンターの値を設定
  inputField.value = counter.toString();
  // カウンターをインクリメント
  counter++;
  // カウンターが1001になったら終了
  if (counter === 1001) {
    console.log('終了しました。');
    clearInterval(intervalId); // インターバルをクリア
  }
}
